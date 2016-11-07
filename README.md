#EXAMPLE TO GET BLOCK FOR ADDRESS
http://geocoding.geo.census.gov/geocoder/geographies/address?street=4600+Silver+Hill+Rd&city=Suitland&state=MD&benchmark=Public_AR_Census2010&vintage=Census2010_Census2010&layers=14&format=json

#RESOURCES TO GET DATA BY BLOCKS
http://api.census.gov/data/2010/sf1.html

## Configuration and Setup

Setup virtual environment
```
$ virtualenv venv 
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create a filed name key.ini as follows
```
[key]
value: YOUR_KEY
```

CSV 'addresses.csv' with fields ordered: id street city state zip

Create a postgres database locally. (first time setup only)
```
$  sudo -u postgres createdb cenus
```

Add the tables to your database
```
$ python models.py
```

## Usage

Get geography for the addresses listed in addresses.csv.  First import the addresses from csv to the DB.
Name the file "addresses.csv" and arrange the columns: id, street, city, state, zipcode
```
$ python import_addresses.py
```
Download query data for each address
```
$ python download_geography.py
```
Parse results and import to DB
```
$ python parse_geography.py
```
Download and then parse block data
```
$ python download_blkdata.py
$ python parse_blkdata.py
```
Export to csv
```
$ python export.py
```





