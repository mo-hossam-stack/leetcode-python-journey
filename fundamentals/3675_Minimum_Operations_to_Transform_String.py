# Problem: Minimum Operations to Transform String
# LeetCode: https://leetcode.com/problems/minimum-operations-to-transform-string/
# Difficulty: Medium

class Solution:
    def minOperations(self, s: str) -> int:
        distinct = set(s)
        res =0
        for ch in distinct:
            steps = (26 - (ord(ch) - ord('a'))) % 26
            res = max(res, steps)
        return res