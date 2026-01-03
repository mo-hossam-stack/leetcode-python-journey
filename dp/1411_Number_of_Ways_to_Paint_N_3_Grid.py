# Problem: Number of Ways to Paint N × 3 Grid
# LeetCode: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
# Difficulty: Hard

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7

        @cache
        def dp(i,a,b,c):

            if i == 0: return 1

            res = 0
            for color_a in range(1, 4):

                    for color_b in range(1, 4):

                            for color_c in range(1,4):

                                if color_a != a and (color_b != color_a and color_b != b) and (color_c != color_b and color_c != c):

                                    res = (res + dp(i-1, color_a, color_b, color_c)) % MOD


            return res

        
        return dp(n, 0,0,0)
