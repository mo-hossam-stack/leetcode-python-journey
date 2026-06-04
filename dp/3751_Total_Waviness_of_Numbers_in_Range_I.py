# Problem: 3751. Total Waviness of Numbers in Range I
# LeetCode: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
# Difficulty: Medium
class Solution:
    MAX = 100001
    dp = [0] * MAX
    pref = [0] * MAX

    # Precomputation block for static global range caching
    for i in range(100, MAX):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10

        isWave = m > max(l, r) or m < min(l, r)
        dp[i] = dp[i // 10] + int(isWave)
        pref[i] = pref[i - 1] + dp[i]

    def totalWaviness(self, A: int, B: int) -> int:
        return self.pref[B] - self.pref[A - 1]
