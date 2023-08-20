class Solution:
    def SumTwo(self, arr, target):
        res = set()
        arr.sort()
        for i in arr:
            if (target - i ) in arr:
                res.add((i, target-i))
                arr.remove(target - i)
        return res
arr = [0,3,2,4,1]
target = 4
s= Solution()
print(s.SumTwo(arr, target))
