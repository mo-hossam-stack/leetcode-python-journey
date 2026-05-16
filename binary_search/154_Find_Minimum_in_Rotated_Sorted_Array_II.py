# Problem: 154. Find Minimum in Rotated Sorted Array II
# LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Difficulty: Hard
class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()

        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]
