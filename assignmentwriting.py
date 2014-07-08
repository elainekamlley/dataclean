#===========================
# assignmentwriting.csv
# Open a python script that assigns 

import csv

Header = ['Name', 'Favorite_Color', 'Favorite_Food', 'First_Crush']
Cassidy = ['Cassidy', 'Lavender', 'Thai','John']
Pam = ['Pam', 'Purple', 'Jambalay', 'Prince']
Selina = ['Selina','Gold', 'Watermelon','Punky Brewster']
Jason = ['Jason','Black and Navy Blue','Peanut Soup','Thelma']



with open('crush_census.csv', 'wb') as csvfile:
    new_writer = csv.writer(csvfile, delimiter=',',quotechar='"')
    for rockstar in [Header, Cassidy, Pam, Selina, Jason,]:
    	new_writer.writerow(rockstar)