'''def compressDNS(str1):
    res = ''
    count = 1
    for char in range(1,len(str1)):
        if str1[char - 1] == str1[char]:
            count += 1
        else:
            if count > 1:
                res += str(count)
            res = res + str1[char - 1]
            count = 1
    if count > 1:
        res += str(count)
    res = res + str1[-1]

    return res

print(compressDNS('ABBCCCDEEEEA'))'''
def compressstring(str1):
    res = ''
    count = 1
    for i in range(1, len(str1)):
        if str1[i - 1] == str1[i]:
            count += 1
        else:
            if count > 1:
                res += str(count)
            res = res + str1[i -1]
            count = 1
    if count > 1:
        res += str(count)
    res = res + str1[-1]

    return res

print(compressstring('ABBCCCDDDDEEFA'))
