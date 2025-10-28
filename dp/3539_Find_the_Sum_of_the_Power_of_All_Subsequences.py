# Problem: Find the Sum of the Power of All Subsequences (Magical Sum)  
# LeetCode: https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/  
# Difficulty: Hard  

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        # time -> O(m^3 * k*n)
        #space -> O(m^2 * k * n)
        MOD = 10**9 + 7
        @cache
        def dp(mask, m, k, i):
            if m == 0 and mask.bit_count() == k: return 1
            if m == 0 or i == len(nums): return 0

            total = 0
            total += (dp(mask >> 1, m, k - (mask & 1), i + 1)) % MOD  # skip i

            for freq in range(1, m + 1):
                nmask = mask + freq
                next_ = (dp(nmask >> 1, m - freq, k - (nmask & 1), i + 1)) % MOD
                total += (
                    pow(nums[i], freq, MOD) * next_  # curr element * next element
                    * comb(m, freq)  # add combinations of freq in m
                ) % MOD

            return total

        return (dp(0, m, k, 0)) % MOD
