# Problem: Power of Four
# LeetCode: https://leetcode.com/problems/power-of-four/
# Difficulty: Easy

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        diff = round(math.log(n, 4)) - math.log(n, 4)
        return abs(diff) < 1e-10
