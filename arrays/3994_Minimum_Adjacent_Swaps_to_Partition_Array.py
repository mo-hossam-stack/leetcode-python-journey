# Problem: 3994. Minimum Adjacent Swaps to Partition Array
# LeetCode: https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/
# Difficulty: Medium

class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        mp = []
        for x in nums:
            if x < a:
                mp.append(0)
            elif a <= x <= b:
                mp.append(1)
            else:
                mp.append(2)
                
        fp = mp 
        
        swaps = count_1 = count_2 = 0 
        
        for t in fp:
            if t == 0:
                swaps = (swaps + count_1 + count_2) % MOD
            elif t == 1:
                swaps = (swaps + count_2) % MOD
                count_1 += 1
            else:
                count_2 += 1
                
        return swaps
