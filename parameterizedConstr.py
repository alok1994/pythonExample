class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self,f,s):
        self.first = f
        self.second = s

    def display(self):
        print("First Number:",self.first)
        print("Second Number:",self.second)
        print("Answer:", self.answer)

    def calculate(self):
        self.answer = self.first + self.second


add = Addition(1000,2000)
add.calculate()
add.display()
