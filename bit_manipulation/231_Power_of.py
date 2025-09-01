# Problem: Power of Two
# LeetCode: https://leetcode.com/problems/power-of-two/
# Difficulty: Easy

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0