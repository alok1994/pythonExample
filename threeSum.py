nums = [-1,1,0,2,3, -2]
target = 1
res = set()
nums.sort()
for i in range(len(nums)):
    left = i + 1
    right = len(nums) -1
    while left < right:
        if nums[i] + nums[left] + nums[right] == target:
            res.add((nums[i], nums[left], nums[right]))
        if nums[i] + nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
print(res)
