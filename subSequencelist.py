inpt = [1,2,3,6,7,10,11,12,13,15,17,18]
output = [[1,2,3],[6,7],[10,11,12,13], [15],[17,18]]
res = []
curr = [inpt[0]]
for x in inpt[1:]:
    if x - 1 != curr[-1]:
        res.append(curr)
        curr = [x]
    else:
        curr.append(x)
res.append(curr)
print(res)

