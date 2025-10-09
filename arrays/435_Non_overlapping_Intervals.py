# Problem: 435. Non-overlapping Intervals
# LeetCode: https://leetcode.com/problems/non-overlapping-intervals/
# Difficulty: Medium


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end= float('-inf')
        count =0
        for start, end in intervals:
            if start>= last_end:
                last_end = end
            else:
                count += 1
        return count