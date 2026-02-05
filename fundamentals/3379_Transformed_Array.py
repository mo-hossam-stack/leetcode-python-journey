# Problem: 3379. Transformed Array
# LeetCode: https://leetcode.com/problems/transformed-array/
# Difficulty: Easy

class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        return [nums[((i + nums[i]) % n + n) % n] for i in range(n)]
