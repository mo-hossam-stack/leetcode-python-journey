# Problem: 1009. Complement of Base 10 Integer
# LeetCode: https://leetcode.com/problems/complement-of-base-10-integer/
# Difficulty: Easy

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if n==0 else n^((1<<n.bit_length())-1)