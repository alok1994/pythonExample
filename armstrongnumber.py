def order(num):
    n = 0
    while num != 0:
        n = n + 1
        num = num // 10
    return n

def armstrong(num):
    ords = order(num)
    temp = num
    sum1 = 0
    while num != 0:
        r = num % 10
        print(r)
        print(r ** ords)
        sum1 += r ** ords
        num = num // 10
    if sum1 == temp:
        print('The given number is {} Armstrong number'.format(temp))
    else:
        print('Not an Armstrong number')

armstrong(1634)
