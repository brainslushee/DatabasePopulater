class Customer:
    def __init__(self, firstName, lastName, emailAddress):
        # default constructor
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setEmailAddress(emailAddress)

    def setFirstName(self, firstName):
        # some validation could be added here
        self.firstName = firstName

    def setLastName(self, lastName):
        # some validation could be added here
        self.lastName = lastName
    
    def setEmailAddress(self, emailAddress):
        # some validation could be added here
        self.emailAddress = emailAddress

    def getFirstName(self):
        return str(self.firstName)

    def getLastName(self):
        return str(self.lastName)
    
    def getEmailAddress(self):
        return str(self.Email)

    def toString(self):
        formatString = "(\"{0}\", \"{1}\", \"{2}\")".format(self.firstName,
                self.lastName, self.emailAddress)
        return formatString
