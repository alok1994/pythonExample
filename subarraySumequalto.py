'''
Subarray Sum Equals K
Given an array of intergers and an interger k, you need to find the total numbers
of continous subarray whose sum equals to k.
'''
class Solution:
    def subArraySum(self, nums, target):
        sumDict = {0:1}
        count = 0
        s = 0
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
s = Solution()
print(s.subArraySum(nums, target))
