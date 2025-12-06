# Problem: 3432 Count Partitions with Even Sum Difference
# LeetCode: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
# Difficulty: Easy

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        suffix = sum(nums)
        n = len(nums)
        prefix = 0
        res = 0
        for i in range(n-1):
            prefix += nums[i]
            suffix -= nums[i]

            if (suffix - prefix)%2==0:res += 1
        
        return res