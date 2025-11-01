# Problem: Running Sum of 1d Array
# LeetCode: https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums