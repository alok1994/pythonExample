# longest substring without repeating characters

class Solution:
    def lenghtOfLongestSubstring(self, st):
        if len(st) == 0:
            return 0
        maps = {}
        max_length = start = 0
        for i in range(len(st)):
            if st[i] in maps:
                start = maps[st[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            maps[st[i]] = i

        return (max_length)

st = 'abcdaefg'
s = Solution()
print(s.lenghtOfLongestSubstring(st))


