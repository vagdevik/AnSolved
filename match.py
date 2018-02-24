import csv

def read_data(): 
	global data
	open_file = open('Data.csv', 'rU')
	csv_reader = csv.reader(open_file)
	data = []
	for element in csv_reader:
		data.append(element[3] + " " + element[0])
	data = data[1:]

