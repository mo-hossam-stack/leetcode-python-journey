# Problem: 2091. Removing Minimum and Maximum From Array
# LeetCode: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
# Difficulty: Medium
class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        left = min(mn, mx)
        right = max(mn, mx)

        front = right + 1

        back = n - left

        frontBack = (left + 1) + (n - right)

        return min(front, back, frontBack)
