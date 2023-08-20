class Solution:
    def compress(self, str1):
        print(str1)
        res = ''
        count = 1
        for i in range(1, len(str1)):
            if str1[i - 1] == str1[i]:
                count += 1
            else:
                if count > 1:
                    res = res + str(count)
                res = res + str1[i-1]
                count = 1
        if count > 1:
            res = res + str(count)
        res = res + str1[-1]
        return res
                
obj = Solution()
print(obj.compress('ABBCCCDDDDEAA'))



def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
       return  n

print(fact(5))
