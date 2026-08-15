# Problem: 3702. Longest Subsequence With Non-Zero Bitwise XOR
# LeetCode: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
# Difficulty: Medium
class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        tot = nz = 0

        for n in nums:
            nz |= n > 0
            tot ^= n

        return nz * (len(nums) - (not tot))
