# Problem: Maximum Subarray
# LeetCode: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(num, dp[i - 1] + num)
        return max(dp)