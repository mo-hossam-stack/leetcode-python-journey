# Problem: 3727. Maximum Alternating Sum of Squares
# LeetCode: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Difficulty: Medium
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted(x * x for x in nums)

        k = len(nums) // 2

        return sum(a[k:]) - sum(a[:k])
