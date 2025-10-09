# Problem: 3701. Compute Alternating Sum
# LeetCode: https://leetcode.com/problems/compute-alternating-sum/
# Difficulty: Easy


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(nums[::2]) - sum(nums[1::2])
