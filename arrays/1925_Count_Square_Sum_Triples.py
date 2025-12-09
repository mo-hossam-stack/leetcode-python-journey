#Problem: Count Square Sum Triples
#LeetCode: https://leetcode.com/problems/count-square-sum-triples/
#Difficulty: Easy
class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            for j in range(i+1 , n+1):
                k = int(sqrt(i**2 + j**2))
                if k <=n and i**2 + j**2 == k**2:
                    res += 2

                    
        return res
