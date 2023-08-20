seq = [1,2,3,4,5,6,7,8,9]
print(list(filter((lambda x: x%2 == 0), seq)))


seq = [1,2,3,4,5,6,7,8,9]
print(list(map((lambda x: x + x ),seq)))
