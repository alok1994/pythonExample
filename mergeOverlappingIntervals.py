'''
GIven a collection of intervals, merge all overlapping intervals
Example 1:
Input: [[1,3],[2,6],[8,10], [15,18]]
Output: [[1,6],[8,10], [15,18]]

Example 2:
Input: [[1,,4], [4,5]]
Output: [[1,5]]
'''
class Solution:
    def merge(self, intervals):
        intervals.sort(key= lambda x: x[0])
        print(intervals)
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals

arr = [[1,3],[8,10],[2,6], [15,18]]
s = Solution()
print(s.merge(arr))
