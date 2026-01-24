# Problem: Minimize Maximum Pair Sum in Array
# LeetCode: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# Difficulty: Medium

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = -inf
        nums.sort()
        for i in range(n//2):
            res = max(res , nums[i] + nums[-i - 1])
        return res
