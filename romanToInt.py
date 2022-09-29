class Solution:
    def romanToInt(self, st):
        curr = 0
        total = 0
        prev = 0
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(st)):
            curr = rom[st[i]]
            if curr > prev:
                total = total + curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total

s = Solution()
print(s.romanToInt('XLIX'))
