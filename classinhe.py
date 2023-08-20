class Name:
    def __init__(self, firstname):
        self.firstname = firstname

    def printName(self):
        print('Name:',self.firstName)

class MiddleName(Name):
    def __init__(self, middlename, firstname):
        self.middlename = middlename
        Name.__init__(self, firstname)

    def printMiddleName(self):
        print('FirstName and MiddleName:', self.firstname, middlename)

class lastName(MiddleName):
    def __init__(self, firstname, middlename, lastname):
        self.lastname = lastname
        MiddleName.__init__(self, middlename, firstname)

    def printFullName(self):
        print('Full Name:', self.firstname, self.middlename, self.lastname)

obj = lastName('Alok', 'Kumar', 'Verma')
obj.printFullName()
