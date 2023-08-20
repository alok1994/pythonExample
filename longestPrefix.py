class Solution:
    def longestCommonPrefix(self, strs):
        res = ''
        for i in zip(*strs):
            if len(set(i)) != 1:
                return res
            res += i[0]

strs = ["flower","flow","flight"]
s = Solution()
print(s.longestCommonPrefix(strs))
