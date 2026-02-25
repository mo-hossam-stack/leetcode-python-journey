# Problem: 1356. Sort Integers by The Number of 1 Bits
# LeetCode: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Difficulty: Easy

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr
