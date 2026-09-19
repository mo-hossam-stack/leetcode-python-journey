# Problem: 1401. Circle and Rectangle Overlapping
# LeetCode: https://leetcode.com/problems/circle-and-rectangle-overlapping/
# Difficulty: Medium
class Solution:
    def checkOverlap(self, r: int, xC: int, yC: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x1-=xC 
        x2-=xC 
        y1-=yC 
        y2-=yC
        D2=0
        D2+=-(x1>0) & x1*x1
        D2+=-(x2<0) & x2*x2
        D2+=-(y1>0) & y1*y1
        D2+=-(y2<0) & y2*y2
        return r*r>=D2
