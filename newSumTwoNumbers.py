ls = [1,3,0,8,7,4,2,5,6]
target = 7
res = set()
ls.sort()
for i in range(len(ls)):
    left = i
    right = len(ls) - 1
    while left < right:
        if ls[left] + ls[right] == target:
            res.add((ls[left], ls[right]))
        if ls[left] + ls[right] < target:
            left +=1
        else:
            right -= 1

print(res)
