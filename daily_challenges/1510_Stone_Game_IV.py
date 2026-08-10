# Problem: 1510. Stone Game IV
# LeetCode: https://leetcode.com/problems/stone-game-iv/
# Difficulty: Hard

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        
        squares = [j * j for j in range(1, int(n ** 0.5) + 1)]
        
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                if not dp[i - sq]:
                    dp[i] = True
                    break
                    
        return dp[n]
