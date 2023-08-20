class A:
    def __init__(self, firstname):
        self.firstname = firstname

    def show(self):
        print("Show FirstName:", self.firstname)

class B(A):
    def __init__(self, middlename, firstname):
        super().__init__(firstname)
        self.middlename = middlename
        
    def show(self):
        super().show()
        print("Show MiddleName:",self.middlename)


obj = B('Kumar', 'Alok')
obj.show()
