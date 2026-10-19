# Problem: 2089. Find Target Indices After Sorting Array
# LeetCode: https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Difficulty: Easy
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans
