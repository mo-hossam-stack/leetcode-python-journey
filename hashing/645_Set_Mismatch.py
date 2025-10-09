# Problem: 645. Set Mismatch
# LeetCode: https://leetcode.com/problems/set-mismatch/
# Difficulty: Easy


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        duplicate = sum(nums) - sum(s)
        missing = sum(range(1, n + 1)) - sum(s)
        return [duplicate, missing]