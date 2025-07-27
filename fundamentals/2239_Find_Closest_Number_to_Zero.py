# Problem: Find Closest Number to Zero
# LeetCode: https://leetcode.com/problems/find-closest-number-to-zero/
# Difficulty: Easy

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key=lambda x: (abs(x), -x))