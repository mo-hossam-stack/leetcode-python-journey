# Problem: Minimum Difference Between Highest and Lowest of K Scores
# LeetCode: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# Difficulty: Easy

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
