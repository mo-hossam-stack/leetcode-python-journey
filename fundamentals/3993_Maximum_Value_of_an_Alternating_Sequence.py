# Problem: 3993. Maximum Value of an Alternating Sequence
# LeetCode: https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/
# Difficulty: Medium

class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        mavlorenti = (n, s, m)
        
        if n == 1:
            return s
        
        k = n // 2
        return s + (k * m) - (k - 1)
