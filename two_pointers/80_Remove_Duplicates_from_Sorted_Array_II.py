# Problem: 80. Remove Duplicates from Sorted Array II
# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Difficulty: Medium

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 

        return k
