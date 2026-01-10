# Problem: Minimum ASCII Delete Sum for Two Strings
# LeetCode: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# Difficulty: Medium

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        dp = [[0] * (m+1) for _ in range(n +1 )]

        for i in range(1 , n+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for j in range(1 , m+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1 ,n+1):
            for j in range(1 , m+1):
                if s1[i -1] == s2[j -1]:
                    dp[i][j] = dp[i-1][j-1] # carry acc val
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]), #remove s1[i-1]
                        dp[i][j-1] + ord(s2[j-1])
                    )
        return dp[-1][-1]
