class Solution:
    def longestCommonSubSequence(self, text1, text2):
        n, m = len(text1), len(text2)
        dp = [ [0]*(m+1) for z in range(n+1)]
        #print(dp)
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        print(dp)
        return dp[-1][-1]

text1 = 'abcde'
text2 = 'ace'
obj = Solution()
print(obj.longestCommonSubSequence(text1, text2))



class Solution:
    def longestCommonPrefix(self,arr):
        if len(arr) == 0:
            return ''
        minl = len(arr[0])

        for i in arr:
            minl = min(minl, len(i))
        lcp = ''
        i = 0
        while i < minl:
            char = arr[0][i]
            for j in range(1, len(arr)):
                if char != arr[j][i]:
                    return lcp
            lcp = lcp + char
            i=i+1
        return lcp

arr = ['flower', 'flow', 'flight']
s = Solution()
print(s.longestCommonPrefix(arr))


def longestPrefix1(arr):
    if len(arr) == 0:
        return ''
    res = ''
    for i in zip(*arr):
        if len(set(i)) != 1:
            return res
        res = res + i[0]
    return res

print(longestPrefix1(arr))


# Longest SubString without repeating  character

def longestSubString(st):
    if len(st) == 0:
        return 0
    maps = {}
    max_length = start = 0
    for i in range(len(st)):
        if st[i] in maps:
            start = maps[st[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        maps[st[i]] = i
    return max_length

print(longestSubString('abcdae'))

def maxSubArray(nums):
    max_sum = max_total = nums[0]
    for i in nums[1:]:
        max_total = max(i, i+ max_total)
        max_sum = max(max_total, max_sum)
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



Input = [[1,3],[2,6],[8,10], [15,18]]
Output: [[1,6],[8,10], [15,18]]

def mergeIntervals(arr):
    arr.sort(key = lambda x: x[0])
    i = 1
    while i < len(arr):
        if arr[i][0] < arr[i-1][1]:
            arr[i-1][0] = min(arr[i-1][0], arr[i][0])
            arr[i-1][1] = max(arr[i-1][1],arr[i][1])
            arr.pop(i)
        i = i + 1
    return arr

print(mergeIntervals(Input))

inputs = [1,2,3,6,7,10,11,12,13,15,17,18]
output = [[1,2,3],[6,7],[10,11,12,13], [15],[17,18]]

def subSequenceList(inputs):
    res = [inputs[0]]
    output = []
    for i in inputs[1:]:
        if i - 1 != res[-1]:
            output.append(res)
            res = [i]
        else:
            res.append(i)
    output.append(res)
    return output
print(subSequenceList(inputs))


class Solution:
    def QuadSum(self, arr, target):
        arr.sort()
        res = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                left = j + 1
                right = len(arr) - 1
                while left < right:
                    sumhere = arr[i] + arr[j] + arr[left] + arr[right]
                    if sumhere == target:
                        res.append((arr[i],arr[j],arr[left],arr[right]))
                        left += 1
                        right -= 1
                    if sumhere < target:
                        left += 1
                    else:
                        right -= 1
        return res

arr = [-1,0,-2,-1,2]
target = 0
s = Solution()
print(s.QuadSum(arr, target))


class Solution:
    def sumThree(self, arr, target):
        res = []
        arr.sort()
        for i in range(len(arr)):
            left = i+ 1
            right = len(arr) -1
            while left < right:
                sumhere = arr[i] + arr[left] + arr[right]
                if sumhere == target:
                    res.append((arr[i],arr[left],arr[right]))
                    left += 1
                    right -= 1
                elif sumhere < target:
                    left +=1
                else:
                    right -=1
        return res

arr = [-1,0,1,-2,-4,2, -3,]
target = 0
s  = Solution()
print(s.sumThree(arr, target))

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumhere = nums[i] + nums[left] + nums[right]
                if abs(sumhere - target) < abs(res - target):
                    res = sumhere
                if sumhere < target:
                    left +=1
                else:
                    right -= 1
        return res


nums= [-1,2,1,-4]
target = 1
s = Solution()
print(s.threeSumClosest(nums,target))
