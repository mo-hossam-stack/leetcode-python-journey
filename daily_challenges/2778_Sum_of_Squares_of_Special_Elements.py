# Problem: 2778. Sum of Squares of Special Elements
# LeetCode: https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Difficulty: Easy
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                ans += nums[i] * nums[i]

        return ans
