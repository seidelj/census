import os, csv, json, pprint
from sqlutils import get_or_create
from sqlalchemy import update

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(PROJECT_DIR, 'retrieved_json')

from models import Address, Geography, Session

e = open("errors.csv", 'w')
e.write("id,user,street,city,state,zipcode,reason\n")
session = Session()

def main():
	count = 0
	for address in session.query(Address).all():
		if parse_json(address):
			count += 1
	session.commit()
	print count


def parse_json(address):
	filename = os.path.join(DOWNLOAD_DIR, "{}.json".format(address.id))
	with open(filename) as jsonFile:
		data = json.load(jsonFile)
		blockList = []
		for match in data['result']['addressMatches']:
			blocks = match['geographies']['Census Blocks'][0]
			blockList.append(blocks['BLOCK'])

		if len(set(blockList)) != 1:
			reason = "no match" if len(set(blockList)) == 0 else "multiple match"
			e.write("'{}','{}','{}','{}','{}','{}','{}'\n".format(
				address.id,
				address.user,
				address.street,
				address.city,
				address.state,
				address.zipcode,
				reason,
			))
		else:
			print filename
			block_info = data['result']['addressMatches'][0]['geographies']['Census Blocks'][0]
			block, created = get_or_create(session, Geography,
				block=block_info['BLOCK'], state=block_info['STATE'],
				county=block_info['COUNTY'], tract=block_info['TRACT'],
				blockgrp=block_info['BLKGRP'], geoid=block_info['GEOID']
			)
			session.commit()
			address.geography_id = block.id

		##	TO SLOW
		#	session.query(Address).filter(address.id==address.id).update({'geography_id': block.id})


if __name__ == "__main__":
	main()
