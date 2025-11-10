# Problem: Minimum Operations to Make Array Non-Decreasing
# LeetCode: https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/
# Difficulty: Medium

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        s = []  # monotonic stack
        for x in nums:
            while s and s[-1] > x:
                s.pop()
            if x == 0:
                continue
            if not s or s[-1] < x:
                s.append(x)
                res += 1
        return res
