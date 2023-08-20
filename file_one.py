import file_two

print('File one __name__: {}'.format(__name__))

if __name__ == '__main__':
    print('File one directly executed')
else:
    print('File one imported and executed')
