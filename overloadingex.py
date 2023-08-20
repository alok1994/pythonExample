# PYTHON doesn't support method overloading like c, it will conside latest define method 
def test(a,b):
    print(a * b)

def test(a,b,c):
    print(a * b * c)

test(2,3)
