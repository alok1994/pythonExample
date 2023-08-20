class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        
        Grandfather.__init__(self,grandfathername)
        
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        Father.__init__(self, fathername, grandfathername)

    def parents(self):
        print("Grandfathername:", self.grandfathername)
        print("Fathername:",self.fathername)
        print("Son name:", self.sonname)

s = Son('Advik', 'Alok', 'Vyas')
s.parents()
