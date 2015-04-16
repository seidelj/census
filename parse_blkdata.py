from ast import literal_eval
import os, sys, json
from sqlutils import get_or_create
from models import Address, Geography, CensusDataBlk, Session

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS = os.path.join(PROJECT_DIR,'blk-data')

session = Session()

def parse_txt_files(geo):
	# Create a new censusdatablk object
	censusdatablk = CensusDataBlk()
	session.add(censusdatablk)
	session.commit()
	# assign the object to appropriate geography objects
	session.query(Geography).filter(Geography.state==geo.state, Geography.county==geo.county, Geography.tract==geo.tract, Geography.blockgrp==geo.blockgrp).update({'censusdatablk_id': censusdatablk.id})
	for variable in CensusDataBlk.__table__.columns.keys():
		if variable == "id":
			continue
		filename = "{}_{}_{}.json".format(variable, geo.state, geo.county)
		f = open(os.path.join(DOWNLOADS, filename), 'r')
		data = json.load(f)	
		parse_json(censusdatablk.id, geo, data, variable)

def parse_json(cid, geo, data, variable):
	geoMatch = "{}{}{}{}".format(geo.state, geo.county, geo.tract, geo.blockgrp)
	for l in data:
		dataMatch = "{}{}{}{}".format(l[2], l[3], l[4], l[5])
		if dataMatch == geoMatch:
			censusdatablk = session.query(CensusDataBlk).filter(CensusDataBlk.id==cid)
			if l[1] == None:
				l[1] = "none"
			censusdatablk.update({variable: l[1]})
	

def main():
	for geo in session.query(Geography).distinct(Geography.state, Geography.county, Geography.tract, Geography.blockgrp):
		parse_txt_files(geo)
	session.commit()
if __name__ == "__main__":
	main()
