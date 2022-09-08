class Solution:
    def pairTwoNumberEqualSubraction(self, arr, S):
        res = set()
        arr.sort()
        for i in range(len(arr)):
            left = i
            right = len(arr) - 1
            while left < right:
                if arr[right] - arr[left] == s:
                    res.add((arr[right], arr[left]))
                    left += 1
                    right -= 1
                elif arr[right] - arr[left] < s:
                    left += 1
                else:
                    right -= 1
        return res
    
arr = [1,4,2,3,9,12,13,0,8]
s = 8
obj = Solution()
print(obj.pairTwoNumberEqualSubraction(arr,s))
