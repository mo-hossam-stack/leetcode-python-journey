# Problem: N-Repeated Element in Size 2N Array
# LeetCode: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Difficulty: Easy

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x = len(nums) // 2
        return (next((n for n, c in Counter(nums).items() if c == x), -1))
