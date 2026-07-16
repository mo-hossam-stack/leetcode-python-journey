# Problem: 3867. Sum of GCD of Formed Pairs
# LeetCode: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
# Difficulty: Medium

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0

        for i in range(len(nums)):
            mx = max(mx, nums[i])
            nums[i] = gcd(mx, nums[i])

        nums.sort()

        left, right = 0, len(nums) - 1
        ans = 0

        while left < right:
            ans += gcd(nums[left], nums[right])
            left += 1
            right -= 1

        return ans
