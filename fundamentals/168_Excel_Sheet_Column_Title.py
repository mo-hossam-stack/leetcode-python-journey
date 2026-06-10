# Problem: 168. Excel Sheet Column Title
# LeetCode: https://leetcode.com/problems/excel-sheet-column-title/
# Difficulty: Easy

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(result[::-1])
