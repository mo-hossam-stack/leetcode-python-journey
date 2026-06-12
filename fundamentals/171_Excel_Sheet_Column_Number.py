# Problem: 171. Excel Sheet Column Number
# LeetCode: https://leetcode.com/problems/excel-sheet-column-number/
# Difficulty: Easy

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord('A') + 1)

        return ans
