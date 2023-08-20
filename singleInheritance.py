class Parents:
    def func1(self):
        print("Function from the Parents class")


class Child(Parents):

    def func2(self):
        print("Function from child class")


obj = Child()
obj.func2()
obj.func1()
