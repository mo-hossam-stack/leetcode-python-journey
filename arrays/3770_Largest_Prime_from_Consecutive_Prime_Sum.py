# Problem: Largest Prime from Consecutive Prime Sum
# LeetCode: https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/
# Difficulty: Medium

class Solution:
    def largestPrime(self, n: int) -> int:
        if n == 1: return 0

        def is_prime(n: int) -> list:

            if n < 2:
                return []

            is_prime = [True] * (n+1)

            is_prime[0] = is_prime[1] = False

            for i in range(2, int(n**0.5) + 1):

                if is_prime[i]:

                    for j in range(i*i, n+1, i):
                        is_prime[j] = False

            return is_prime

        is_prime = is_prime(n)
        primes = [i for i in range(n+1) if is_prime[i]]

        sum_consec_prime = acc = 0
        for i in range(len(primes)):
            acc += primes[i]
            if acc > n: break

            if is_prime[acc]:
                sum_consec_prime = acc

        return sum_consec_prime