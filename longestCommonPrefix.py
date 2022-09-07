'''Write a function to find the longest common
prefix string amongest an array of strings
If there is no common prefix, return an empty string 
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        minlen = len(strs[0])
        for i in range(len(strs)):
            minlen = min(len(strs[i]), minlen)

        lcp = ''
        i = 0
        while i < minlen:
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return lcp
            lcp = lcp + char
            i +=1
        return lcp

strs= ['flower', 'flow', 'flight']
s = Solution()
print(s.longestCommonPrefix(strs))


'''------- -------------------------------'''
class Solutions:
    def longestCommonPrefixs(self, strs):
        if len(strs) == 0:
            return ""
        lcp = ""
        for i in zip(*strs):
            if len(set(i)) != 1:
                return lcp
            lcp = lcp + i[0]

        return lcp

s = Solutions()
print(s.longestCommonPrefixs(strs))
