# Problem: 3578 Count Partitions With Max Min Difference at Most K
# LeetCode: https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/
# Difficulty: medium

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dp(i, mn, mx):
            if i == n: 
                return mx - mn <= k

            mn = min(mn, nums[i])
            mx = max(mx, nums[i])

            if mx-mn > k: 
                return 0

            else:

                return (dp(i+1, inf, -inf) + dp(i+1, mn, mx)) % (10**9+7)

        return dp(0, inf,-inf)//2 # because at index n-1, we split into 2 branches...