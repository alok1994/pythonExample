class Solution:
    def sumThree(self, arr, target):
        res = []
        arr.sort()
        for i in range(len(arr)):
            left = i + 1
            right = len(arr) -1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append((arr[i], arr[left],arr[right]))
                    while left < right and arr[left] == arr[left + 1]:
                        left +=1
                    while left < right and arr[right] == arr[right -1 ]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

arr = [-1,0,1,-2,-4,2, -3,]
target = 0
s  = Solution()
print(s.sumThree(arr, target))
