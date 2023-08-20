def func(arg1, *args, **kwargs):
    print('First arg', arg1)
    for arg in args:
        print(arg)
    for i,j in kwargs.items():
        print(i,j)
func('alok', 'Welcome', 'to', 'GeekForGeek', firstname='alok', secondname='verma')
