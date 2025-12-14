# Problem: Number of Ways to Divide a Long Corridor
# LeetCode: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
# Difficulty: Hard

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        MOD = 10**9 + 7
        s= 0
        for c in corridor:
            if c == 'S':s+=1
        if not s or s%2 == 1 :return 0

        res = 1
        l = 0
        while l < n:
            r = l
            s = 0
            while r < n and s <2:
                if corridor[r] == 'S':s+= 1
                r +=1

            p = 0
            while   r <n and corridor[r] == 'P':
                p +=1
                r +=1
            
            if r != n and p:
                res = (res * (p+1)) % MOD
            l =r
        return res
