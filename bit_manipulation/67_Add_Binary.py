# Problem: 67. Add Binary
# LeetCode: https://leetcode.com/problems/add-binary/
# Difficulty: Easy

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a , 2) + int(b , 2))[2:])
