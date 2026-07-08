# Problem: 3756. Concatenate Non-Zero Digits and Multiply by Sum II
# LeetCode: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
# Difficulty: Medium

MOD, MAX = 1000000007, 100005
pow10 = [1] * MAX
for i in range(1, MAX):
    pow10[i] = (pow10[i - 1] * 10) % MOD

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        
        A = [0] * (n + 1)
        compact_prefix = [0] * (n + 1)
        nz_count = [0] * (n + 1)
        
        nz_idx = 0
        for i in range(n):
            d = int(s[i])
            A[i + 1] = A[i] + d
            
            if d > 0:
                compact_prefix[nz_idx + 1] = (compact_prefix[nz_idx] * 10 + d) % MOD
                nz_idx += 1
            
            nz_count[i + 1] = nz_idx

        res = []
        for l, r in queries:
            cnt_l = nz_count[l]
            cnt_r = nz_count[r + 1]
            
 
            if cnt_l == cnt_r:
                x = 0
            else:
                num_digits = cnt_r - cnt_l
                sub = (compact_prefix[cnt_l] * pow10[num_digits]) % MOD
                x = (compact_prefix[cnt_r] - sub) % MOD
            
       
            digit_sum = A[r + 1] - A[l]
            
            res.append((x * digit_sum) % MOD)
            
        return res
