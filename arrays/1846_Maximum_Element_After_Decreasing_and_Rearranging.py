# Problem: 1846. Maximum Element After Decreasing and Rearranging
# LeetCode: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
# Difficulty: Medium

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()

        arr[0] = 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]
