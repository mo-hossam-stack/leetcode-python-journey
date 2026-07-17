# Problem: 801. Minimum Swaps To Make Sequences Increasing
# LeetCode: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# Difficulty: Hard

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap = [0] * n
        noswap = [0] * n
        swap[0] = 1
        for i in range(1, n):
            strictly_increasing = A[i] > A[i-1] and B[i] > B[i-1]
            strictly_xincreasing = A[i] > B[i-1] and B[i] > A[i-1]
            
            if strictly_increasing and strictly_xincreasing:                               
                swap[i] = min(noswap[i-1], swap[i-1]) + 1
                noswap[i] = min(noswap[i-1], swap[i-1])
            
            elif strictly_increasing:
                swap[i] = swap[i-1] + 1
                noswap[i] = noswap[i-1]
              
            elif strictly_xincreasing:
                swap[i] = noswap[i-1] + 1
                noswap[i] = swap[i-1]
                        
        return min(noswap[n-1], swap[n-1])
