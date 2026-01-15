# Problem: Maximize Area of Square Hole in Grid
# LeetCode: https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/
# Difficulty: Medium

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def f(bars):
            res = 0
            bars = list(sorted(bars))
            curr = 1
            prev = -1
            for b in bars:
                if b == prev + 1:
                    curr += 1
                else:
                    curr = 1
                prev = b
                res = max(res, curr)
            return res
        
        l = f(hBars)
        w = f(vBars) 
        s = min(l, w)
        return (s + 1) ** 2
