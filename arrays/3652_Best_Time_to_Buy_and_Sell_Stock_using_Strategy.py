#Problem: 3652 Best Time to Buy and Sell Stock using Strategy
#LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/
#Difficulty: Medium

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        res = sum(s*p for s,p in zip(strategy, prices))
        window = sum(prices[k//2:k]) + sum(s*p for s,p in zip(strategy[k:], prices[k:]))
        res = max(res, window)

        for i in range(n-k):

            window += strategy[i] * prices[i] - prices[i+k//2] + prices[i+k] - strategy[i+k] * prices[i+k]

            res = max(res, window)
        return res
        