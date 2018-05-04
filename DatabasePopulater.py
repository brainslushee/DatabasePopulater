# Author: Kyle Mayer
# Date: 5/3/2018
#Python version: >3.6


import random
from Customer import *

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

        firstName = ""
        lastName = ""
        email = ""

        for i in range(1, amount):
            #---------- create customer object
            customer = Customer(firstName, lastName, email)

            #----------- select randomly from each respective list
            randFirstNamesIndex = random.randint(0, len(self.firstNames) - 1)
            randLastNamesIndex = random.randint(0, len(self.lastNames) - 1)
            domainName = self.domainNames[i % len(self.domainNames)]

            #----------- set first name/last name
            customer.setFirstName(self.firstNames[randFirstNamesIndex])
            customer.setLastName(self.lastNames[randLastNamesIndex])

            #----------- create email address
            # create email in format of first letter of first name plus last name
            randomNum = random.randint(1, 100)
            email = customer.getFirstName()[0] + \
                    customer.getLastName() + \
                    str(((i * 1000000) % randomNum) * 34 + 1) + \
                    "@" + domainName  
                    
            customer.setEmailAddress(email) 
    
       
            #----------- append to list
            self.customerList.append(customer.toString())

    
    def writeCustomerFile(self):
        '''
        Method writeCustomerFile writes the whole list of random customers generated with createRandomCustomers 
        to a file named customerList.txt
        '''
        f = open("customerList.txt", "a+")
        
        for customer in self.customerList:
           f.write(customer + "\n") 

        f.close()        
