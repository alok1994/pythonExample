def smartDivide(func):
    def inner(a,b):
        print('Going to divide {} via {}'.format(a,b))
        if b == 0:
            print('Ohhh! cann\'t divide by zero')
            return
        return func(a,b)
    return inner

@smartDivide
def divide(a,b):
    print(a/b)


divide(4,0)
