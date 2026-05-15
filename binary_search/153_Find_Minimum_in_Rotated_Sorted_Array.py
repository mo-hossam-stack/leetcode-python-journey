# Problem: 153. Find Minimum in Rotated Sorted Array
# LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]
