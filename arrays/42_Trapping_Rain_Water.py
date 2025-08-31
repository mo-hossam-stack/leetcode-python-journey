# Problem: Trapping Rain Water
# LeetCode: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        maxL = [0] * n
        maxR = [0] * n

        maxL[0] = height[0]
        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i])

        maxR[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(maxL[i], maxR[i]) - height[i]

        return ans