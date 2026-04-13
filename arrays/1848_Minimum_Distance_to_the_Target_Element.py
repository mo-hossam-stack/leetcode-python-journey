# Problem: 1848. Minimum Distance to the Target Element
# LeetCode: https://leetcode.com/problems/minimum-distance-to-the-target-element/
# Difficulty: Easy

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("inf")
        n= len(nums)

        for i in range(n):
            if nums[i] == target:
                res = min(res , abs(start - i))
        return res
