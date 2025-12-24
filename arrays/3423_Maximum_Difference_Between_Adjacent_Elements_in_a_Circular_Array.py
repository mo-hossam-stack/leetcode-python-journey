# Problem: Maximum Difference Between Adjacent Elements in a Circular Array
# LeetCode: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
# Difficulty: Easy

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n =  len(nums)
        mx = abs(nums[0] - nums[n-1])
        for i in range(1, n):
            mx = max(mx , abs(nums[i] - nums[i-1]))
        return mx
