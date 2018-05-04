# Author: Kyle Mayer
# Date: 5/3/2018
# Purpose: 
    # This was originally intended for populating a database for a CS class project, but
    # I used it to practice object oriented programming, file I/O, and random generation
    # with Python.
#Python version: >3.6

#TODO:
    #could read in each list from a file
    #add file reader to read in each name

from DatabasePopulater import *

def readFiles(filename):
    # list to store values and return from function
    names = []

    # read in file and strip newlines from each line
    with open(filename) as f:
        names = f.read().splitlines()

    f.close()

    # returns a list
    return names


firstNames = readFiles("resources/firstNames.txt")
lastNames = readFiles("resources/lastNames.txt")
domainNames = readFiles("resources/domainNames.txt")


dbPop = DatabasePopulater(firstNames, lastNames, domainNames)

dbPop.createRandomCustomers(1000)

dbPop.writeCustomerFile()


print("List of first names, last names, and email addresses")
print ("generated and written to file: customerList.txt")
