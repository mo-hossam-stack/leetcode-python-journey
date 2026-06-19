# Problem: 1732. Find the Highest Altitude
# LeetCode: https://leetcode.com/problems/find-the-highest-altitude/
# Difficulty: Easy

class Solution:
    def largestAltitude(self, gain):
        n = len(gain)
        mx = 0

        for i in range(n + 1):
            alt = 0
            for j in range(i):
                alt += gain[j]
            mx = max(mx, alt)

        return mx
