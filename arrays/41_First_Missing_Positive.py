# Problem: First Missing Positive
# LeetCode: https://leetcode.com/problems/first-missing-positive/
# Difficulty: Hard

class Solution:
    def firstMissingPositive(self, nums):
        temp = set(nums)
        max_num = max(nums) if nums and max(nums) > 0 else 1
        for i in range(1, max_num + 2):
            if i not in temp:
                return i