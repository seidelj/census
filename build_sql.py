"""
This file appends models.py with tables for the variables listed
in variables.csv
"""

#1) Build a temporary text file containing the table to be added
#2) Append that to the exisiting models.py

import os, sys, csv

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_FILE = os.path.join(PROJECT_DIR, 'models_temp.py')
MODELS_FILE = os.path.join(PROJECT_DIR, 'models.py')
filename = "variables.csv"


def read_csv(filename):
	variables = []
	with open(filename, 'rb') as f:
		mycsv = csv.reader(f)
		next(mycsv, None)
		for row in mycsv:
			variables.append(row[0])
	return variables


def write_to_temp_file(variables):
	classLine = "\nclass CensusDataBlk(Base):"
	tableNameLine = "\n\t__tablename__ = 'censusdatablk'"
	idLine = "\n\tid = Column(Integer, Sequence('censusdatablk_id_seq'), primary_key=True)"
	columnLines = ""
	for variable in variables:
		columnLines += "\n\t{} = Column(String)".format(variable)
	columnLines += "\n"
	target = open(TEMP_FILE, 'w')
	target.write(classLine)	
	target.write(tableNameLine)
	target.write(idLine)
	target.write(columnLines)
	target.close()

def merge_temp():
	finalLine = "Base.metadata.create_all(engine)"
	target = open(MODELS_FILE, 'r+')
	for line in target.readlines():
		print line
		if finalLine in line:
			line.replace(finalLine, "")
	target.close()
	target = open(MODELS_FILE, "a+")
	target_temp = open(TEMP_FILE, "r")
	target.write('\n')
	for line in target_temp:
		target.write(line)
	target.write("\n{}".format(finalLine))
		

def main():
	variables = read_csv(filename)
	write_to_temp_file(variables)
	merge_temp()

if __name__ == "__main__":
	main()

