# Problem: Add Binary
# LeetCode: https://leetcode.com/problems/add-binary/
# Difficulty: Easy

class Solution:
    def addBinary(self, a, b):
        sum_bin = bin(int(a, 2) + int(b, 2))[2:]
        return sum_bin