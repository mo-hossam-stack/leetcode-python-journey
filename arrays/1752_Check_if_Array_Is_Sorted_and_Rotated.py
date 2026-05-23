# Problem: 1752. Check if Array Is Sorted and Rotated
# LeetCode: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Difficulty: Easy
class Solution:
    def check(self, nums: list[int]) -> bool:
        ok = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                ok += 1

        return ok <= 1
