#Problem: Complete Prime Number
#LeetCode: https://leetcode.com/problems/complete-prime-number/
#Difficulty: Medium

class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n: int) -> bool:

            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False

            i = 3

            while i * i <= n:
                if n % i == 0:return False

                i += 2
            return True
        s= str(num)
        n = len(s)

        for i in range(n):
            if not is_prime(int(s[:i+1])):
                return False
            
            if not is_prime(int(s[n-1-i:])):

                return False
        return True
