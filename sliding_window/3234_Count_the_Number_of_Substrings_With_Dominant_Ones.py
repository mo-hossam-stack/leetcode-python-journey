# Problem: Count the Number of Substrings With Dominant Ones
# LeetCode: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
# Difficulty: Medium

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        
        prefix_ones = [0] * (n + 1)
        
        for i in range(n):
            prefix_ones[i] = prefix_ones[i-1] + int(s[i] == '1')
        
        zeros = [i for i in range(n) if s[i] == '0']
                
        res = 0
        for K in range(int(sqrt(n))+1):
            num_zeros = 0
            l = 0
            idx_zeros = 0
            for r in range(n):
                num_zeros += s[r] == '0'
                
                while num_zeros > K:
                    num_zeros -= s[l] == '0'
                    
                    if s[l] == '0':
                        idx_zeros += 1
                    l += 1

                if num_zeros == K and prefix_ones[r] - prefix_ones[l-1] >= K*K:
                    #ones = 0
                    # if idx_zeros == len(zeros):
                    #     ones = 0
                    if idx_zeros == 0 and zeros:
                        ones = zeros[idx_zeros]
                    elif 1 <= idx_zeros < len(zeros):
                        ones = prefix_ones[zeros[idx_zeros]] - prefix_ones[zeros[idx_zeros-1]]
                    else:
                        ones = 0
                        
                    excess = prefix_ones[r] - prefix_ones[l-1] - K*K
                    if K == 0:
                        res += excess
                    else:
                        res += min(ones, excess) + 1
                    
        return res