# Problem: Separate Squares I
# LeetCode: https://leetcode.com/problems/separate-squares-i/
# Difficulty: Medium

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l, r = 0.0, 10**9

        while r - l > 1e-5:
            m = (l + r) / 2

            below = 0
            above = 0

            for _, y, side in squares:
                if y <= m:
                    below += (min(m, y + side) - y) * side
                if y + side >= m:
                    above += ((y + side) - max(m, y)) * side

            if below >= above:
                r = m
            else:
                l = m

        return l
