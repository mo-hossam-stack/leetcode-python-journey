# Problem: Minimum Time Visiting All Points
# LeetCode: https://leetcode.com/problems/minimum-time-visiting-all-points/description/
# Difficulty: Easy


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res=0
        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            res+=max( abs(y1 - y2 ) ,abs(x1-x2) )
            x1,y1 = x2,y2
        return res