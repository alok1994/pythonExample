class Solution:
    def reverseNum(self, number):
        rev = 0
        remain = 0
        while number > 0:
            remain = number % 10
            rev = rev * 10 + remain
            number = number // 10
        return rev

s = Solution()
print(s.reverseNum(12345))
