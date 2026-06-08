# Problem: 215. Kth Largest Element in an Array
# LeetCode: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
