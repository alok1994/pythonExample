'''def smartDivide(func):
    print("From Decorator")
    def inner(a,b):
        if b == 0:
            print('can not divide with zero')
            return
        print("a and b value", a, b) 
        return func(a,b)
    return inner

@smartDivide
def divide(a,b):
    print(a/b)
    print('From function')


divide(4,0)'''

'''def smartdivide(func):
    def inner(a,b):
        print('Going to divide {} by {}'.format(a,b))
        if b == 0:
            print('Can not divide by zero')
            return
        return func(a,b)
    return inner 

@smartdivide
def divide(a,b):
    print(a/b)

divide(4,2)'''
def smartDivide(func):
    def inner(a,b):
        print('Going to divide {} by {}'.format(a,b))
        if b == 0:
            print('Not divide by zero')
            return
        return func(a,b)
    return inner


@smartDivide
def divide(a,b):
    print(a/b)

divide(4,0)
