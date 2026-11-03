# Problem: 3736. Minimum Moves to Equal Array Elements III
# LeetCode: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# Difficulty: Medium
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(max(nums) - nums[i] for i in range(len(nums)))
