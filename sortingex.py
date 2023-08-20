ls1 = [10,9,3,1,4,6,12,0]
newls = []
while ls1:
    minimum = ls1[0]
    for item in ls1:
        if item < minimum:
            minimum = item

    newls.append(minimum)
    ls1.remove(minimum)
print(newls)
