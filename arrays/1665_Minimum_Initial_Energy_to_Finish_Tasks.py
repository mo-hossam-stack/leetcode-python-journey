# Problem: 1665. Minimum Initial Energy to Finish Tasks
# LeetCode: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
# Difficulty: Hard
class Solution:
    def minimumEffort(self, shop: List[List[int]]) -> int:
        shop.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        start = shop[0][1]
        bal = shop[0][1] - shop[0][0]
        loan = 0

        for i in range(1, len(shop)):
            cost, thresh = shop[i]
            
            if bal < thresh:
                loan += thresh - bal
                bal = thresh
                
            bal -= cost

        return start + loan
