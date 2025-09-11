# Problem: Power of Three
# LeetCode: https://leetcode.com/problems/power-of-three/
# Difficulty: Easy

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        diff = round(math.log(n, 3)) - math.log(n, 3)
        return abs(diff) < 1e-10