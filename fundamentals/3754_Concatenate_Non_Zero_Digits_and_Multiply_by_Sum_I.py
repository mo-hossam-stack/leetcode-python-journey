# Problem: 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# LeetCode: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
# Difficulty: Easy

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(c) for c in str(n) if c != '0']
        x = int(''.join(map(str, digits))) if digits else 0
        return x * sum(digits)
