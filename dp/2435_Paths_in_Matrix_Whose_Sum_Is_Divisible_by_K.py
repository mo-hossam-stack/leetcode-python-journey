# Problem: Paths in Matrix Whose Sum Is Divisible by K
# LeetCode: https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
# Difficulty: Hard

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * k for _ in range(m)] for _ in range(n)] 
        dp[0][0][grid[0][0] % k] = 1



        for i in range(n):
            for j in range(m):
                if i ==0 and j ==0:continue
                for r in range(k):
                    prev = (r - grid[i][j]) % k
                    if i ==0:dp[i][j][r] += dp[i][j-1][prev]


                    elif j ==0: dp[i][j][r] += dp[i-1][j][prev]
                    else:
                        dp[i][j][r] += (dp[i-1][j][prev] + dp[i][j-1][prev] ) % MOD
        
        return dp[-1][-1][0]
