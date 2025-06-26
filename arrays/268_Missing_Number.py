# Problem: Missing Number
# LeetCode: https://leetcode.com/problems/missing-number/description/
# Difficulty: Easy

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
