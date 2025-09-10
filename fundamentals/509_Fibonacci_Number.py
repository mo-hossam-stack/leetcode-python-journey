# Problem: Fibonacci Number
# LeetCode: https://leetcode.com/problems/fibonacci-number/
# Difficulty: Easy

class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        fib_n = (phi**n - psi**n) / sqrt5
        return int(fib_n)
