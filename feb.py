def feb(limit):
    a,b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

#for i in feb(5):
#    print(i,end= ' ')


def new(limit):
    a,b = 0,1
    while a < limit:
        print(a, end=' ')
        a,b = b, a+ b

new(5)
