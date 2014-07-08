#============================== 
#datacleanup.py
#
#Script that reads in event_signups.csv cleans the data, and writes it back out
#as event_signups_clean.csv
#==============================
#Testing Suite:
#
#Test 1: If script can read in csv and print row 1 as a list, then pass
#Test 2: If script can read, and print all values in upper case, then pass
#Test 3: If script prints out every unique event name and they are all for unique events, pass
#Test 4: If script is able to read a list generated in the script and print write to csv, If script is able to read a list generated in the 			script and write to "event_signups_clean.csv", pass
#Test 5: IF script writes "event_signups_clean.csv" and rows 664, 824, and 9 have correct event names, pass
#==============================

# Section 1.0
#------------------
# This code is to import the current file event_signups.csv and print the first row
# csv.reader is an object that you can use to manipulate csv to read it
import csv

# This will be a lists of list. Each item will represent a new row that will be 
# written in the new CSV
new_file_contents = []

with open('event_signups.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
	#stores the header information
	header = event_file_reader.next()
	#print header <-- Test 1
	
	#creates new header for new CSV
	new_header = [header[0], header[1], header[2], header[3], header[4], header[5], header[6]]

	# print new_header <-- Mini Test
	new_file_contents.append(new_header)
	
	for row in event_file_reader:
		#print row[0].upper() <-- Test 2
		if row[0] == 'GRASSROOTS LOBBY DAY':
			row[0]= 'LOBBY DAY'
			print row[0]
		if row[0] == 'GRASSROOTS LOBBYING DAY':
			row[0]= 'LOBBY DAY'
			print row[0]
		new_row = [row[0].upper(), row[1],row[2], row[3], row[4], row[5], row[6]]
		new_file_contents.append(new_row)



#===============================================
#writes the new file 
with open('event_signups_clean.csv', 'wb') as csvfile:
		new_csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"')
		for row in new_file_contents:
			new_csv_writer.writerow(row)

