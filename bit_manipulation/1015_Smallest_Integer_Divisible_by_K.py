# Problem: Smallest Integer Divisible by K
# LeetCode: https://leetcode.com/problems/smallest-integer-divisible-by-k/
# Difficulty: Medium

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
