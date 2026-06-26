# Problem: 324. Wiggle Sort II
# LeetCode: https://leetcode.com/problems/wiggle-sort-ii/
# Difficulty: Medium

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
