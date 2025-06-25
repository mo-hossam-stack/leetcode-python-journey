# Problem: Contains Duplicate
# LeetCode: https://leetcode.com/problems/contains-duplicate/
# Category: Array / Hashing / Set
# Difficulty: Easy

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))