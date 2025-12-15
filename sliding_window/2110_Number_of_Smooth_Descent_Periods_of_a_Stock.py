# Problem: Number of Smooth Descent Periods of a Stock
# LeetCode: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
# Difficulty: Medium

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        l = 0

        while l < n:
            r = l+1
            while r < n and prices[r] == prices[r - 1] -1:
                r += 1
            res += comb(r - l +1 , 2)
            l = r
        
        return res
