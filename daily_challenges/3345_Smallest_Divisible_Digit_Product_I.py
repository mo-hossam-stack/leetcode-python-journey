# Problem: 3345. Smallest Divisible Digit Product I
# LeetCode: https://leetcode.com/problems/smallest-divisible-digit-product-i/
# Difficulty: Easy

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            x = n

            while x > 0:
                product *= x % 10
                x //= 10

            if product % t == 0:
                return n

            n += 1
