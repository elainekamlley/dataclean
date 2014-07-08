# ===========================
# readingcsv.py
# This script opens a csv file, imports its data row by row. It will print from a 
# comma separate value from one column onto the screen (for each row)
#=============================

# Python uses 'packages' to hold a set of tools you don't use all the time
# But you can import them when you need them. CSV is a package of tools for working on CSVs

# Import package to run a csv file
import csv

with open('fellows_fun_census.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
	for row in event_file_reader:
		if row[2] == " ":
			row[2] = ", The King in the North"
		print "{0} {1} {2} is a fellow. They are from {3} and want to be a {4}" .format(row[0],row[1], row[2], row[3], row[4])

# Working with a csv file always has these parts:
	# A line (like line 13) to open the file that tells the computer which files you want to open
	# and some options to help it understand how that file is laid out.
	
	# A line (like line 14) that tells Python how to save the info from the csv in its own language
	# We use a delimiter to tell Python on how each value is separated
	# A quotechar = '"' treats the value like a string ex. keeps addresses together

	# A line (like line 15) that starts the for loop that will cycle through all the rows 	



