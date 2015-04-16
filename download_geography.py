import sys, os
import urllib2
import ConfigParser
from models import Session, Address

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(PROJECT_DIR, 'retrieved_json')
session = Session()

### Get key ###
config = ConfigParser.ConfigParser()
try:
	config.read('key.ini')
	key = config.get('key', 'value')
except ConfigParser.NoSectionError:
	sys.exit("Improperly configured key.ini file")

url_fixes = [
	'http://geocoding.geo.census.gov/geocoder/geographies/address?street=',
	'&city=',
	'&state=',
	'&benchmark=Public_AR_Census2010&vintage=Census2010_Census2010&layers=14&format=json'
]

def main():
	create_download_folder()
	for address in session.query(Address).all():
		download_json(address)

def create_download_folder():
	if not os.path.isdir(DOWNLOAD_FOLDER):
		print "Making %s" % DOWNLOAD_FOLDER
		os.mkdir(DOWNLOAD_FOLDER)

def download_json(address):
	new_file = os.path.join(DOWNLOAD_FOLDER, "{}.json".format(address.id))
	if not os.path.exists(new_file):
		html = retrieve_json(address)
		if html:
			save_file(html, new_file)
	else:
		print "Already downloaded {}".format(new_file)

def retrieve_json(address):
	url = url_fixes[0] + address.street.replace(" ","+") + \
		url_fixes[1] + address.city.replace(" ","+") + url_fixes[2] + \
		address.state + url_fixes[3]
	html = None
	try:
		response = urllib2.urlopen(url)
		if response.code == 200:
			print "Downloading {}".format(url)
			html = response.read()
		else:
			print "Invalid Url: {}".format(url)
	except urllib2.HTTPError:
		print "Failed to open {}".format(url)
	return html


def save_file(html, filename):
	try:
		with open(filename, 'w') as f:
			f.write(html)
	except IOError:
		print "Could not write to file {}".format(filename)


if __name__ == "__main__":
	main()
