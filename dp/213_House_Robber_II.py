# Problem: 213. House Robber II
# LeetCode: https://leetcode.com/problems/house-robber-ii/
# Difficulty: Medium
class Solution:
    def rob(self, nums: List[int]) -> int:

        def robbing(nums: List[int]) -> int:

            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):

                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + nums[i]
                )

            return max(dp)

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            robbing(nums[:n - 1]),
            robbing(nums[1:])
        )
