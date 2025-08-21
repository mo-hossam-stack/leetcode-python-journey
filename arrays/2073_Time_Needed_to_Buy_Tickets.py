# Problem: Time Needed to Buy Tickets  
# LeetCode: https://leetcode.com/problems/time-needed-to-buy-tickets/  
# Difficulty: Easy  

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)
        return res
