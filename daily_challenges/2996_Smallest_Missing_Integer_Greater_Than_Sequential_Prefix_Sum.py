# Problem: 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
# LeetCode: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# Difficulty: Easy

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        seen = set(nums)

        ans = total
        while ans in seen:
            ans += 1
        return ans
