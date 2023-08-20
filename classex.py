class A:
    def __init__(self, name):
        self.name = name
        
    def test(self):
        print("class A", self.name)
        
class B(A):
    def __init__(self, bname, name):
        A.__init__(self, name)
        self.bname = bname
        
    def test(self):
        super().test()
        print("class B", self.bname)
        

class C(B,A):
    def __init__(self, cname, bname, name):
        B.__init__(self, bname, name)
        self.cname = cname
        
    def test(self):
        super().test()
        print("class c", self.cname)



c = C("c class", "b class", "a class")
c.test()
