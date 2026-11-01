# Problem: 453. Minimum Moves to Equal Array Elements
# LeetCode: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Difficulty: Medium
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
