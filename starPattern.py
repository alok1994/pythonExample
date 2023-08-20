rows = 6
sp = 1
for i in range(rows, 0, -1):
    for space in range(1, sp):
        print(' ',end='')
    for j in range(1, i+1):
        print('*', end= ' ')
    print(' ')
    sp =sp + 1
