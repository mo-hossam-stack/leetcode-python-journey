# Problem: 921. Minimum Add to Make Parentheses Valid
# LeetCode: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Difficulty: Medium
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        add = 0
        for c in s:
            if c == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    add += 1
        return add + open
