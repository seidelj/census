import csv, os
from models import Session, Address, Geography, CensusDataBlk

session = Session()
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
filenames = ['address.csv', 'data.csv']

def main():
	fieldsDict = get_field_names()
	with open(os.path.join(PROJECT_DIR, 'address.csv'),'w') as f:
		write_address_csv(fieldsDict['address'], f)
	with open(os.path.join(PROJECT_DIR, 'data.csv'), 'w') as f:
		write_data_csv(fieldsDict['census'], f)
	print "Finished"	


def write_address_csv(modelinfo, f):
	writer = csv.writer(f, csv.excel)
	header = modelinfo + ['data_id']
	writer.writerow(header)
	for address in session.query(Address).all():
		objList = []
		geo = session.query(Geography).filter(Geography.id==address.geography_id).first()
		try:
			data_id = geo.censusdatablk_id
		except AttributeError:
			data_id = 'no census match'
		for field in modelinfo:
			objList.append(getattr(address, field))
		objList.append(data_id)
		writer.writerow(objList)

def write_data_csv(modelinfo, f):
	writer = csv.writer(f, csv.excel)
	header = ['data_id'] + modelinfo[1:]
	writer.writerow(header)
	for data in session.query(CensusDataBlk).all():
		objList = []
		for field in modelinfo:
			objList.append(getattr(data, field))
		writer.writerow(objList)



def get_field_names():
	addressFields = []
	for c in Address.__table__.columns:
		addressFields.append(c.name)
	
	dataFields = []
	for c in CensusDataBlk.__table__.columns:
		dataFields.append(c.name)

	fieldDict = {
		'address': addressFields,
		'census': dataFields,
	}

	return fieldDict

if __name__ == "__main__":
	main()
