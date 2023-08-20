print('file two ___name__:{}'.format(__name__))

if __name__ == '__main__':
    print('file two directly executed')
else:
    print('file two imported and executed')
