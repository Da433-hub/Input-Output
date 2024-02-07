with open('DOB.txt', 'r+') as file:# The 'with open () as file:' function opens and closes the file automatically.
    lines = file.read()

file = open('DOB.txt', 'r+')# 'file.readlines()' puts all of the data in the .txt file into list form
lines = file.readlines()

print('\033[1m' + 'Name' + '\033[0m')# Name heading: "\033[1m" adds bold print.

for line in lines: # The for-loop uses .split and .strip to make the list of names into individual indexed words.
    temp = line.strip() # The temp variable stands for 'temporary' list - files created for manipulating the text.
    temp = temp.split() # Split gives individual words in the file an index position.

    print(temp[0] + ' ' + temp[1]) # Print your chosen word order using the indexes; 0 & 1 for the first names and surnames.

print('') # Creates a space between Names and Birthdates lists.

print('\033[1m' + 'Birthdate' + '\033[0m') # Bold birthdate heading.

for line in lines:# For loop with .strip and .split functions again, for indexing the 'Birthdates' list.
    temp = line.strip()
    temp = temp.split()
    print(temp[2] + ' ' + temp[3] + ' ' + temp[4]) # Print the desired data.  The 5 temps stand for the following: 0.First name, 1.Surname, 2.Day, 3.Month and 4.Year
file.close() # Explicitly close the file to release system resources.