def powers(counts):
    n = 2.0
    print(n)
    item = 0
    while n <= counts:
        i = 2+item
        n = 2.0 ** i
        print(n)
        item += 1
        
powers(40)

