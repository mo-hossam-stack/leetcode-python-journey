# Problem: 693. Binary Number with Alternating Bits
# LeetCode: https://leetcode.com/problems/binary-number-with-alternating-bits/
# Difficulty: Easy

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
