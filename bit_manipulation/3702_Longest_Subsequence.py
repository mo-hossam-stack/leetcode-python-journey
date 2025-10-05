# Problem: Longest Subsequence With Limited Sum
# LeetCode: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
# Difficulty: Medium


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if all(num == 0 for num in nums):
            return 0
        return n - 1 if reduce(xor, nums) == 0 else n
