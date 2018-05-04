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




dbPop = DatabasePopulater(firstNames, lastNames, domainNames)

dbPop.createRandomCustomers(1000)

dbPop.writeCustomerFile()
