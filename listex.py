l1 = [[1,2], [3,4], [5,6], [7,8]]
l2 = [[9,10], [11,12], [13,14],[15,16]]

# l3 = [[10,12],[14,16], [18, 20], [22, 24]]
l3 = []
for value1, value2 in zip(l1,l2):
    l4 = []
    for value3 in range(len(value1)):
        sumn = value1[value3] + value2[value3]
        l4.append(sumn)
    l3.append(l4)

print(l1)
print(l2)
print(l3)
        
