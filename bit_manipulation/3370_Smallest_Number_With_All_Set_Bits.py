# Problem: Smallest Number With All Set Bits  
# LeetCode: https://leetcode.com/problems/smallest-number-with-all-set-bits/  
# Difficulty: Easy  

class Solution:
    def smallestNumber(self, n: int) -> int:
        num_bits = floor(log2(n)) + 1
        return 2 ** num_bits-1