# Problem: Minimum Absolute Difference
# LeetCode: https://leetcode.com/problems/minimum-absolute-difference/
# Difficulty: easy

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        ret = []
        for i in range(1, len(arr)):
            min_diff = min(min_diff , arr[i] - arr[i-1])
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) == min_diff:
                ret.append([arr[i-1], arr[i]])
        return ret