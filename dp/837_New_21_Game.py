# Problem: New 21 Game
# LeetCode: https://leetcode.com/problems/new-21-game/
# Difficulty: Medium

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        window_sum = 1.0
        res = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]
            else:
                res += dp[i]

            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return res
