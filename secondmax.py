ls = [41,0,4,2,10,23,9,55]
fmax = ls[0]
smax = ls[0]
for i in range(1, len(ls)):
    if ls[i] > fmax:
        smax = fmax
        fmax = ls[i]
    elif ls[i] > smax and ls[i] != fmax:
        smax = ls[i]
print(smax)

