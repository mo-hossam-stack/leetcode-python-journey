# Problem: 122. Best Time to Buy and Sell Stock II
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Difficulty: Medium
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        HOLD_STOCK, KEEP_CASH = 0, 1

        dp = {}

        dp[-1, HOLD_STOCK] = -math.inf

        dp[-1, KEEP_CASH] = 0

        for day, stock_price in enumerate(prices):

            dp[day, HOLD_STOCK] = max( dp[day-1, HOLD_STOCK], dp[day-1, KEEP_CASH] - stock_price)

            dp[day, KEEP_CASH] = max( dp[day-1, KEEP_CASH], dp[day-1, HOLD_STOCK] + stock_price)
        
        last_day = len(prices)-1
        return dp[last_day, KEEP_CASH]
