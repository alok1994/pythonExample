num = 31
flag = False
for item in range(2, num):
    if num % item == 0:
        flag = True
        break
if flag:
    print('Not prime number')
else:
    print('Prime number')
