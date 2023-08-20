def primeNumber(num):
    flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
        else:
            continue
    if flag:
        print('Not prime')
    else:
        print('Prime')
primeNumber(27)



def primeList(num):
    primeList = []
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primeList.append(i)

    return set(primeList)

print(primeList(50))

