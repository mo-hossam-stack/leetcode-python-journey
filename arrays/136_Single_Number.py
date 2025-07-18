# Problem: Single Number.
# LeetCode: https://leetcode.com/problems/single-number/
# Difficulty: Easy

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            res ^= num
        return res