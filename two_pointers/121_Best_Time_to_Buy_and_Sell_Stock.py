# Problem: Best Time to Buy and Sell Stock
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Difficulty: easy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP=0
        while r!=len(prices):
            if prices[r] > prices[l]:
                prof = prices[r] - prices[l]
                maxP=max(maxP , prof)
            else:
                l = r
            r+=1
        return maxP