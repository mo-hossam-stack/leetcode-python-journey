# Problem: Find First and Last Position of Element in Sorted Array
# LeetCode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Difficulty: Medium

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        
        # Lower Bound: First occurrence
        left, right = 0, n - 1
        lb = n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                lb = mid
                right = mid - 1
            else:
                left = mid + 1
        
        left, right = 0, n - 1
        ub = n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                ub = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if lb <= ub - 1:
            return [lb, ub - 1]
        
        return [-1, -1]
