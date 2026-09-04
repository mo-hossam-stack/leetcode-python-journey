# Problem: 3903. Smallest Stable Index I
# LeetCode: https://leetcode.com/problems/smallest-stable-index-i/
# Difficulty: Easy
class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        suffix = [0] * n
 
        mn = float('inf')
        for i in range(n - 1, -1, -1):
            mn = min(mn, nums[i])
            suffix[i] = mn
 
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            score = mx - suffix[i]
            if score <= k:
                return i
 
        return -1
