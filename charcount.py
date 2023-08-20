str1 = 'Hello World'
d = {}
for i in str1:
    k = d.keys()
    if i in k:
        d[i] += 1
    else:
        d[i] = 1
print(d)
