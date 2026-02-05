# Problem: 65. Valid Number
# LeetCode: https://leetcode.com/problems/valid-number/
# Difficulty: Hard

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(match(r'[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$', s))
