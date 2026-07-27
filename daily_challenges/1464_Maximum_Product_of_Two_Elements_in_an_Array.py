# Problem: 1464. Maximum Product of Two Elements in an Array
# LeetCode: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Difficulty: Easy

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return (nums[n-1] - 1) * (nums[n-2] - 1)
