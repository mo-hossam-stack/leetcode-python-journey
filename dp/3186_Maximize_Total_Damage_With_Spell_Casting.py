# Problem: Maximize Total Damage With Spell Casting
# LeetCode: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
# Difficulty: Medium


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        A = sorted(freq.keys())
        A += [inf, inf, inf]
        
        @cache
        def dp(i):
            if i == -1:
                return 0
            res = freq[A[i]]* A[i]
            for k in range(1,4):
                if A[i - k]<A[i] - 2:
                    res += dp(i - k)
                    break
            return max(dp(i - 1), res)

        return dp(len(A) - 1)
