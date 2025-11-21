# Problem: Set Intersection Size At Least Two
# LeetCode: https://leetcode.com/problems/set-intersection-size-at-least-two/
# Difficulty: Hard

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        times = set()
        intervals.sort(key=lambda x: x[1])
        for s,e in intervals:
            overlap =0
            for t in times:
                if s <=t<= e:
                    overlap+= 1
            while overlap<2:
                if e not in times:
                    times.add(e)
                    overlap += 1
                e -= 1
        return len(times)