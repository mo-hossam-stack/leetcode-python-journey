# Problem: Minimum Penalty for a Shop
# LeetCode: https://leetcode.com/problems/minimum-penalty-for-a-shop/
# Difficulty: Medium

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        bal = 0
        min_bal = 0
        res = 0
        
        for i, c in list(enumerate(customers)) + [(len(customers), '')]:
            if bal < min_bal:
                min_bal = bal
                res = i
            bal += 1 if c == 'N' else -1

        return res
