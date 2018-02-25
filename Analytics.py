import csv
import Levenshtein

def read_data(): 
	global data
	open_file = open('Data.csv', 'rU')
	csv_reader = csv.reader(open_file)
	data = []
	for element in csv_reader:
		data.append(element[3] + " " + element[0])
	data = data[1:]

def find_groups():
	count = 0
	l = len(data)
	flag = [0]*l
	for i in range(0, l):
		if flag[i] == 0:
			print data[i]
			for j in range(i+1, l):
				if flag[j] == 0:
					k1 = match_names(data[i], data[j])
					k2 = match_names(data[j], data[i])
					if k1 == 'True' or k2 == 'True':
						print data[j]
						flag[j] = 1
			count+=1
			flag[i] = 1
			print '\n'
	print count
	
def match_names(name1, name2):
	name1_words = [w.strip('.') for w in name1.split(' ')]
	name2_words = [w.strip('.') for w in name2.split(' ')]
	index = -1
	p = 0
	count1 = 0
	count2 = 0
	for i in range(len(name1_words)):
	    try:
	        index = name2_words[p:].index(name1_words[i])
	        p = index + p + 1
	        count1+=1
	    except:
	        index = -1
	    if index == -1:
	        if len(name2_words[p:])!=0:
	        	char = name1_words[i][0]
	        	for j in range(p, len(name2_words)):
	        	    if char == name2_words[j][0]:
	        	    	if len(name2_words[j])==1:
	        	        	p = j
	        	        	count2+=1
	        	        elif len(name1_words[i])!=1 and len(name2_words[j])!=1:
	        	        	ratio = Levenshtein.ratio(name1_words[i], name2_words[j])
	        	        	if (1-ratio)*len(name2_words[j]) == 1:
	        	        		p = j
	        	        		count2+=1
	        	        	else:
	        	        		return 'False'
	if count1 == 0 or min(len(name1_words), len(name2_words)) > count1 + count2:
		return 'False'
	else:
		return 'True'
		
read_data()
find_groups()
