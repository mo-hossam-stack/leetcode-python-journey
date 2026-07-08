# Problem: 204. Count Primes
# LeetCode: https://leetcode.com/problems/count-primes/
# Difficulty: Medium

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i*i:n:i] = [0] * len(range(i*i, n, i))
                
        return sum(is_prime)
