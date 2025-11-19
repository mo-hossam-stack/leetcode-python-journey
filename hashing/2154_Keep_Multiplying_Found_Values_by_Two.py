# Problem: Keep Multiplying Found Values by Two
# LeetCode: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
# Difficulty: Easy

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original