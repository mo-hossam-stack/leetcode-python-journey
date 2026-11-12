# Problem: 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# LeetCode: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# Difficulty: Easy
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        for i in range(n):
            j = i
            while(j < n -1  and nums[j] < nums[j+1]):
                j += 1
            ans = max(ans , j - i + 1)
            if j > i:
                i = j
            else:
                while(j < n -1  and nums[j] > nums[j+1]):
                    j += 1
                ans = max(ans , j - i + 1)
                i = j
        return ans
