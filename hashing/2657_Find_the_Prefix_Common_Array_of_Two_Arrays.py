# Problem: 2657. Find the Prefix Common Array of Two Arrays
# LeetCode: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# Difficulty: Medium
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        seen = [0] * (n + 1)
        
        for i in range(n):
            seen[0] += seen[A[i]]
            seen[A[i]] = 1
            
            seen[0] += seen[B[i]]
            seen[B[i]] = 1
            
            res[i] = seen[0]
            
        return res
