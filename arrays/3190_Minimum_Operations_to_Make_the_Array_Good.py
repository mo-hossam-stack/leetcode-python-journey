# Problem: Minimum Operations to Make the Array Good
# LeetCode: https://leetcode.com/problems/minimum-operations-to-make-the-array-good/
# Difficulty: Easy

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(num % 3, 3 - num % 3) for num in nums)
        