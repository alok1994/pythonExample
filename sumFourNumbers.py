class Solution:
    def QuadSum(self, arr, target):
        res = []
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                    left = j + 1
                    right = len(arr) -1
                    while left < right:
                        total = arr[i] + arr[j] + arr[left] + arr[right]
                        if total == target:
                            res.append((arr[i], arr[j], arr[left], arr[right]))
                            left += 1
                            right -= 1
                        elif total < left:
                            left += 1
                        else:
                            right -= 1
        return res

arr = [-1,0,-2,-1,2]
target = 0
s = Solution()
print(s.QuadSum(arr, target))
