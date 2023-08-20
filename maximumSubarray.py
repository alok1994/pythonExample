'''
Given an integer array nums,find the contiguous subarray(containing at least one number)
which has the largest sum and return it sum.
'''
'''
Example:
    input: [-2,1,-3,4,-1,2,1,-5,4]
    output: 6
'''

class Solution:
    def maxSubArray(self, nums):
        max_sum = max_total = nums[0]
        for i in nums[1:]:
            max_total = max(i, i+ max_total)
            max_sum = max(max_sum, max_total)
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))



