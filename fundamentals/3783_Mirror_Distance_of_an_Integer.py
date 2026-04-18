# Problem: 3783. Mirror Distance of an Integer
# LeetCode: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Difficulty: Easy

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(int(str(n)[::-1]) - n)
