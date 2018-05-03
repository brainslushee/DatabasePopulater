# Author: Kyle Mayer
# Date: 5/3/2018
#Python version: >3.6


import random

class DatabasePopulater:
    def __init__(self, firstNames, lastNames, domainNames):
        #--------- constructor

        #firstNames, lastNames, and domainNames are all lists
        self.firstNames = firstNames
        self.lastNames = lastNames
        self.domainNames = domainNames
        self.customerList = []

    def createRandomCustomers(self, amount):
        '''
        Method createRandomCustomers creates a list of pseudo-random customers
                @param: amount
                        Pass the amount of customers to generate
         '''
        for i in range(1, amount):
            #----------- select randomly from each respective list
            randFirstNamesIndex = random.randint(0, len(self.firstNames) - 1)
            randLastNamesIndex = random.randint(0, len(self.lastNames) - 1)
            domainName = self.domainNames[i % len(self.domainNames)]

            #----------- first name/last name
            firstName = self.firstNames[randFirstNamesIndex]
            lastName = self.lastNames[randLastNamesIndex]

            #----------- create email address
            # create email in format of first letter of first name plus last name
            randomNum = random.randint(1, 100)
            email = firstName[0] + lastName + str(((i * 1000000) % randomNum) * 34 + 1) + "@" + domainName 

            #---------- format entire string
            #format into a string for to work with INSERT statement
            randomCustomer = "(\"{0}\", \"{1}\", \"{2}\")".format(firstName, lastName, email)
        
            #----------- append to list
            self. customerList.append(randomCustomer)

    
    def writeCustomerFile(self):
        '''
        Method writeCustomerFile writes the whole list of random customers generated with createRandomCustomers 
        to a file named customerList.txt
        '''
        f = open("customerList.txt", "a+")
        
        for customer in self.customerList:
           f.write(customer + "\n") 

        f.close()        