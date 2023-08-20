'''Given an array nums of n integers and integer target, find three integers in nums
such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.'''

'''
Example:

Given array nums =[-1,2,1,-4] and target = 1
The sum that is closest to the target is 2. (-1+2+1 = 2).
'''
#[-4,-1,1,2]

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums) -2):
            left = i + 1
            right = len(nums) -1
            while left < right :
                sumhere = nums[i] + nums[left] + nums[right]
                if abs(sumhere - target) < abs(res - target):
                    res = sumhere
                if sumhere < target:
                    left += 1
                else:
                    right -=1
        return res
nums= [-1,2,1,-4]
target = 1
s = Solution()
print(s.threeSumClosest(nums,target))
