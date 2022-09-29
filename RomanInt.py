class Solution:
    def RomanToInt(self, strs):
        rDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        z = 0
        p = ''
        for i in list(reversed(strs)):
            if p == '':
                 z= z + rDict[i]
            elif rDict[p] <= rDict[i]:
                z = z + rDict[i]
            elif rDict[p] > rDict[i]:
                z = z - rDict[i]
            p = i
        return z

s = Solution()
print(s.RomanToInt('IV'))
