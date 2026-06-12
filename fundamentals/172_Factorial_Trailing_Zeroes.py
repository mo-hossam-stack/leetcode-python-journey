# Problem: 172. Factorial Trailing Zeroes
# LeetCode: https://leetcode.com/problems/factorial-trailing-zeroes/
# Difficulty: Easy

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
