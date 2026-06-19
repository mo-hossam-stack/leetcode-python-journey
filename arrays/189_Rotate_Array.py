# Problem: 189. Rotate Array
# LeetCode: https://leetcode.com/problems/rotate-array/
# Difficulty: Medium

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
