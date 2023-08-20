class Mother:
    mothername = ''
    def mother(self):
        print(self.mothername)

class Father:
    fathername = ''
    def father(self):
        print(self.fathername)

class son(Mother,Father):
    def parents(self):
        print('father:',self.fathername)
        print("mother:",self.mothername)

s = son()
s.mothername = "Ram"
s.fathername = "Sita"
s.parents()
