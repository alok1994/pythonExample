l = [64,12,19,121,129,50,64,90,13,17,23]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l [j]:
            l[i], l[j] = l[j], l[i]
print(l)
