# Problem: 3622. Check Divisibility by Digit Sum and Product
# LeetCode: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Difficulty: Easy
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n % (sum(map(int, str(n))) + __import__('math').prod(map(int, str(n)))) == 0
