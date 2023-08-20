class Person:
    def __init__(self, personname, personage):
        self.personname = personname
        self.personage = personage

    def showage(self):
        print("age", self.personage)

    def showname(self):
        print("name", self.personname)

class Student:
    def __init__(self,studentid):
        self.id = studentid

    def getID(self):
        return self.id

class Resident(Person, Student):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)
        

r = Resident('ALok', '29', '123')
print(r.getID())
r.showage()
