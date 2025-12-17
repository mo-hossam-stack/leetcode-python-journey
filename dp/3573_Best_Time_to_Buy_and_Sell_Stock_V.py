# Problem: 3573. Best Time to Buy and Sell Stock V
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/description/
# Difficulty: medium

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        if n == 0 or k == 0:
            return 0


        dp = [[0] * (k + 1) for _ in range(n)]

        opt_buy = [[float('-inf')] * (k + 1) for _ in range(n)]

        opt_sell = [[float('-inf')] * (k + 1) for _ in range(n)]


        for i in range(n):
            for t in range(1, k + 1):
                if i > 0:
                    opt_buy[i][t] = max(opt_buy[i-1][t], dp[i-1][t-1] - prices[i])

                else:
                    opt_buy[i][t] = -prices[i]

                if i > 0:
                    opt_sell[i][t] = max(opt_sell[i-1][t], dp[i-1][t-1] + prices[i])

                else:
                    opt_sell[i][t] = prices[i]
                if i > 0:
                    dp[i][t] = max(
                        dp[i-1][t],

                        opt_buy[i-1][t] + prices[i],

                        opt_sell[i-1][t] - prices[i]
                    )


        return dp[n-1][k]
