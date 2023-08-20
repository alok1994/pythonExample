number = int(input('Enter number:'))
flag = False
for i in range(2, number):
    if number % i == 0 :
        flag = True
        break
if flag:
    print('Not prime')
else:
    print('prime')


new = []
for item in range(1,100):
    for i in range(2,item):
        if item % i == 0:
            break
    else:
        new.append(item)

print(new)
    
