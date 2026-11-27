# Problem: 3946. Maximum Number of Items From Sale I
# LeetCode: https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
# Difficulty: Medium
class Solution:
    def maximumNumberOfItems(self, items: list[list[int]], budget: int) -> int:
        if not items or budget <= 0:
            return 0

        dp = [0] * (budget + 1)
        min_price = min(price for _, price in items)

        for i, (factor_i, price_i) in enumerate(items):
            free_cnt = sum(
                1
                for j, (factor_j, _) in enumerate(items)
                if i != j and factor_j % factor_i == 0
            )
            gain = 1 + free_cnt
            for b in range(budget, price_i - 1, -1):
                if dp[b - price_i] + gain > dp[b]:
                    dp[b] = dp[b - price_i] + gain

        return max(dp[b] + (budget - b) // min_price for b in range(budget + 1))
