# Problem: Majority Element
# LeetCode: https://leetcode.com/problems/majority-element/
# Difficulty: Easy

class Solution:
    def majorityElement(self, nums):
        h = {}  # val, count
        for num in nums:
            h[num] = h.get(num, 0) + 1

        for key, val in h.items():
            if val > len(nums) // 2:
                return key