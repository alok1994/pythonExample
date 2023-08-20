def longestString(text1, text2):
    n,m = len(text1), len(text2)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]


text1 = "abcde"
text2 = "ace"
print(longestString(text1, text2))


def longestPrefix(strs):
    minlen = len(strs[0])
    for i in strs[1:]:
        minlen = min(minlen, len(i))
    lcp = ''
    i = 0
    while i < minlen:
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return lcp
        lcp = lcp + char
        i = i+ 1
    return lcp
    
strs = ['flower','flow', 'flight']
print(longestPrefix(strs))


def testPrefix(strs):
    res = ''
    for i in zip(*strs):
        if len(set(i)) != 1:
            return res
        else:
            res = res + i[0]
    return res

strs = ['flower','flow', 'flight']
print(testPrefix(strs))



def longestSubString(st):
    max_length = 0
    start = 0
    maps = {}
    for i in range(len(st)):
        if st[i] in maps:
            start = maps[st[i]] + 1
        else:
            max_length = max(max_length, i-start+1)
        maps[st[i]] = i
    return max_length

st = 'abcdabcefg'
print(longestSubString(st))


def maximumSubArray(arr):
    max_total = max_sum = arr[0]
    for i in arr[1:]:
        max_total = max(i, i+max_total)
        max_sum = max(max_sum, max_total)
    return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubArray(arr))

def overlapping(inter):
    i = 1
    while i < len(inter):
        if inter[i-1][1] > inter[i][0]:
            inter[i-1][0] = min(inter[i-1][0],inter[i][0])
            inter[i-1][1] = max(inter[i-1][1],inter[i][1])
            inter.pop(i)
        i = i+ 1
    return inter

inter = [[1,3],[2,6],[8,10], [15,18]]
print(overlapping(inter))
