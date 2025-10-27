# Problem: Number of Laser Beams in a Bank  
# LeetCode: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/  
# Difficulty: Medium  

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        res =0
        for row in bank:
            curr = sum(1 if x== '1' else 0 for x in row)
            if curr > 0:
                res += curr *prev
                prev = curr
        return res