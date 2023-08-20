class Solution:
    def sumOfQuad(self, nums, target):
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) -1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                    if nums[i] + nums[j] + nums[left] + nums[right] <  target:
                        left += 1
                    else:
                        right -= 1
        return list(result)

nums=[-1,0,-2,-1,2]
target = 0
s = Solution()
print(s.sumOfQuad(nums, target))
