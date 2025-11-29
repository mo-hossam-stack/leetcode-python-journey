# Problem: Minimum Operations to Make Array Sum Divisible by K
# LeetCode: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Difficulty: Easy

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
