rows = 6
space= rows
for i in range(1,rows):
    for sp in range(1, space):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end=' ')
    print(' ')
    space = space - 1
