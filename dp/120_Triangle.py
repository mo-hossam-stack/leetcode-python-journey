# Problem: Triangle
# LeetCode: https://leetcode.com/problems/triangle/
# Difficulty: Medium

from functools import cache
from math import inf
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i == len(triangle):
                return 0
            if j == len(triangle[i]):
                return inf
            return triangle[i][j] + min(dp(i + 1, j), dp(i + 1, j + 1))
        return dp(0, 0)