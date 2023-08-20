str1 = 'alok kumar verma'
d = {}
for i in str1:
    key = d.keys()
    if i != ' ':
        if i in list(key):
            d[i] += 1
        else:
            d[i] = 1
print(d)
new_d = sorted(d.items(), key=lambda x:x[0])
print(new_d)
