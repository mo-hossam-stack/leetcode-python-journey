# Problem: 1406. Stone Game III
# LeetCode: https://leetcode.com/problems/stone-game-iii/
# Difficulty: Hard

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n, stonesum = len(stoneValue), sum(stoneValue)
        ssum = [stonesum]
        for val in stoneValue: ssum.append(ssum[-1] - val)
        dp = [[0] * 3 for _ in range(n+1)]
        for sid in range(n, -1, -1):
            for take in range(3):
                dp[sid][take] = ssum[sid] - max(dp[min(sid+take+1, n)])
        alice = max(dp[0])
        bob = ssum[0] - alice
        return "Alice" if alice > bob else ("Bob" if bob > alice else "Tie")
