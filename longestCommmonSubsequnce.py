# Longest Common Subsequence
''' 
Given two string text1 and text2, return the lenght if their longest common
Subsequnce.

A subsequence of a string is a new string generated fron the original string
with some characters(can be none) delete without changing the relative order of the
remaining characters.(eg "ace" is a subsequence of "abcde" while "aec" is not). A
Common subsequence of two strings is a subsequence that is common to both strings.
'''

class Solution:
    def longestCommonSubsequence(self, text1 , text2):
        n,m = len(text1), len(text2)
        dp = [[0]*(m+1) for z in range(n+1)]
        for i in range(n):
            for j in range(m):
                #import pdb;pdb.set_trace()
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    import pdb;pdb.set_trace()
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[-1][-1]

text1 = "abcde"
text2 = "ace"
s = Solution()
print(s.longestCommonSubsequence(text1, text2))

