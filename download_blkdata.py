import sys, os
import urllib2
import ConfigParser
from models import Session, Geography, CensusDataBlk

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS = os.path.join(PROJECT_DIR, 'blk-data')
session = Session()

### Get Key ###
config = ConfigParser.ConfigParser()
try:
	config.read('key.ini')
	key = config.get('key', 'value')
except ConfigParser.NoSectionError:
	sys.exit("Improperly configured key.ini file")

url_fixes = [
	'http://api.census.gov/data/2013/acs5?get=NAME,',
	'&for=block+group:*&in=state:',
	'+county:', '&key='
]

def create_download_folder(folder):
	if not os.path.isdir(folder):
		print "Making {}".format(folder)
		os.mkdir(folder)

def prepare_download(vDict):
	new_file = os.path.join(DOWNLOADS, "{}_{}_{}.json".format(vDict['variable'], vDict['state'], vDict['county']))
	if not os.path.exists(new_file):
		html = download_txt(vDict)
		if html:
			save_file(html, new_file)
	else:
		print "Already downloaded {}".format(new_file)
	
def download_txt(vDict):
	url = url_fixes[0] + vDict['variable'] + \
		url_fixes[1] + vDict['state'] + url_fixes[2] + \
		vDict['county'] + url_fixes[3] + key
	print url
	html = None
	try:
		response = urllib2.urlopen(url)
		if response.code == 200:
			print "Downloaded {}".format(url)
			html = response.read()
		else:
			print "Invalid URL: {}".format(url)
	except urllib2.HTTPError:
		print "Failed to open {}".format(url)
	return html

def save_file(html, filename):
	try:
		with open(filename, 'w') as f:
			f.write(html)
	except IOError:
		print "Could not write to file {}".format(filename)

def main():
	for state, county in session.query(Geography.state, Geography.county).distinct():
		for variable in CensusDataBlk.__table__.columns.keys():
			if variable == "id":
				continue
			vDict = {
				'variable': str(variable),
				'state': state,
				'county': county,
			}
			create_download_folder(DOWNLOADS)
			prepare_download(vDict)


if __name__ == "__main__":
	main()
