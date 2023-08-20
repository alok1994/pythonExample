def func(arg, *args1, **kwargs):
    print('Arg:',arg)
    for arg in args1:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

args = ('first', 'second', 'third')
kwargs = ['first':1, 'second':2, 'third':3}
func('Arg', *args, **kwargs)


print('------------------------------')
def func1(arg, *args, **kwargs):
    print(arg)
    print(args)
    print(kwargs)

func1('alok', 'kumar', 'verma', first=1, second=2, third=3)
