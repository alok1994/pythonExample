class Solution:
    def romanToInt(self, s: str) -> int:
        rDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        z = 0
        p = ""
        for x in list(reversed(s)):
            if p == "":
                z = z + rDict[x]
            elif rDict[p] <= rDict[x]:
                z = z + rDict[x]
            elif rDict[p] > rDict[x]:
                z = z - rDict[x]
            p = x
        return z

s = Solution()
print(s.romanToInt("III"))
