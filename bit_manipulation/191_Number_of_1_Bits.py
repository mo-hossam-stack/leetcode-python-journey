# Problem: 191. Number of 1 Bits
# LeetCode: https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

        return res
