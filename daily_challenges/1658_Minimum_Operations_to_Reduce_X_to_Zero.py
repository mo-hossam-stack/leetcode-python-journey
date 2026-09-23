# Problem: 1658. Minimum Operations to Reduce X to Zero
# LeetCode: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Difficulty: Medium
class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        s = 0
        ans = -1

        for right in range(n):

            s += nums[right]

            while left <= right and s > target:
                s -= nums[left]
                left += 1

            if s == target:
                ans = max(ans, right - left + 1)

        return -1 if ans == -1 else n - ans
