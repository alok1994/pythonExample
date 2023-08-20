def longestCommonString(text1, text2):
    n, m = len(text1), len(text2)
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
print(longestCommonString(text1,text2))


def longestCommonPrefix(strs):
    minlen = len(strs[0])
    for i in strs[1:]:
        minlen = min(minlen, len(i))
    lcp = ''
    n = 0
    while n < minlen:
        char = strs[0][n]
        for j in range(1, len(strs)):
            if char != strs[j][n]:
                return lcp
        else:
            lcp = lcp + char
        n = n + 1
    return lcp

strs= ['flower', 'flow', 'flight']
print(longestCommonPrefix(strs))


def longestSubString(st):
    mp = {}
    max_len = start = 0
    for i in range(len(st)):
        if i in mp:
            start = mp[st[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        mp[st[i]] = i
    return max_len

st = 'abcdaefg'
print(longestSubString(st))


def maxSubArray(nums):
    max_sum = max_total = nums[0]
    for i in nums:
        max_total = max(i, i + max_total)
        max_sum = max(max_sum, max_total)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

def mergeIntervals(arr):
    arr.sort(key=lambda x:x[0])
    i = 1
    while i < len(arr):
        if arr[i-1][1] >= arr[i][0]:
            arr[i-1][0] = min(arr[i-1][0], arr[i][0])
            arr[i-1][1] = max(arr[i-1][1], arr[i][1])
            arr.pop(i)
        i = i +1
    return arr
#arr = [[1,3],[8,10],[2,6], [15,18]]
arr = [[1,4], [4,5]]
print(mergeIntervals(arr))

def romanInt(st):
    total = 0
    prev = 0
    curr = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(st)):
        curr = rom[st[i]]
        if curr > prev:
            total = total + curr - 2 * prev
        else:
            total = total + curr
        prev = curr

    return total
st = 'XLIX'
print(romanInt(st))

dig = 12345
res = 0
while dig > 0:
    rem = dig % 10
    res = res*10 + rem
    dig = dig //10
print(res)


def subSequenceList(arr):
    curr = [arr[0]]
    res = []
    for i in arr[1:]:
        if i - 1 != curr[-1]:
             res.append(curr)
             curr = [i]
        else:
            curr.append(i)
    res.append(curr)
    return res

inpt = [1,2,3,6,7,10,11,12,13,15,17,18]
print(subSequenceList(inpt))

def subArrEqual(nums, target):
    sumDict = {0:1}
    s = 0
    count = 0
    for num in nums:
        s += num
        if s - target in sumDict:
            count += sumDict[s - target]
        if s in sumDict:
            sumDict[s] += 1
        else:
            sumDict[s] = 1
    return count

nums = [3,4,7,2,-3,1,4,2,1]
target = 7
print(subArrEqual(nums, target))

def QuadSum(arr, target):
    arr.sort()
    res = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            left = j + 1
            right = len(arr) - 1
            while left < right:
                s = arr[i] + arr[j] + arr[left] + arr[right]
                if s == target:
                    res.add((arr[i],arr[j] , arr[left] , arr[right]))
                    left += 1
                    right -= 1
                if s < target:
                    left += 1
                else:
                    right -= 1
     
                        
    return res

arr = [-1,0,-2,-1,2]
target = 0
print(QuadSum(arr, target))
