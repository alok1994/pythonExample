rows = int(input("Enter the number of rows:"))
space = rows 
for i in range(1, rows+1):
    for j in range(1,space):
        print(' ', end='')
    for k in range(1,i+1):
        print('*', end=' ')
    print(' ')
    space= space - 1
