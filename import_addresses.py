import csv, os
from models import Session, Address
from sqlutils import get_or_create

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

session = Session()

def main():
	filename = os.path.join(PROJECT_DIR, 'addresses.csv')
	import_to_sql(filename)

def import_to_sql(filename):
	with open(filename, 'rb') as f:
		mycsv = csv.reader(f)
		next(mycsv, None)
		for row in mycsv:
			address, created = get_or_create(session, Address,
				user=row[0],
				street = row[1].replace("#", "unit").replace(".",""),
				city = row[2],
				state = row[3],
				zipcode = row[4],
			)
		session.commit()

if __name__ == "__main__":
	main()
