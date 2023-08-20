ls = [0,1,2,3,4,5,6,7,8]
# output = [0,9,1,8,2,7,3,6,4,5]
ls1 = []
num = len(ls) - 1
for i in range(len(ls)-1):
    while i <= num:
        ls1.append(i)
        ls1.append(ls[num])
        break
    num = num -1

print(ls1)

