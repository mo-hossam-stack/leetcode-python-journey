# Problem: 1680. Concatenation of Consecutive Binary Numbers
# LeetCode: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# Difficulty: Medium

class Solution:
    def concatenatedBinary(self, n: int) -> int:       
        MOD = 10**9 + 7
        res = bits = 0

        for i in range(1, n+1):
            if (i & (i-1)) == 0:
                bits += 1
            res = ((res << bits) | i) %MOD

        return res
