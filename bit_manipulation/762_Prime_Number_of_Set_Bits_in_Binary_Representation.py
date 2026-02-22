# Problem: 762. Prime Number of Set Bits in Binary Representation
# LeetCode: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Difficulty: Easy

class Solution(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in range(L, R+1))
