#EXAMPLE TO GET BLOCK FOR ADDRESS
http://geocoding.geo.census.gov/geocoder/geographies/address?street=4600+Silver+Hill+Rd&city=Suitland&state=MD&benchmark=Public_AR_Census2010&vintage=Census2010_Census2010&layers=14&format=json

#RESOURCES TO GET DATA BY BLOCKS
http://api.census.gov/data/2010/sf1.html

## Configuration and Setup

Create a filed name key.ini as follows

```
[key]
value: YOUR_KEY
```

CSV 'addresses.csv' with fields ordered: id street city state zip

Create a postgres database locally.

```
$ python models.py
```



