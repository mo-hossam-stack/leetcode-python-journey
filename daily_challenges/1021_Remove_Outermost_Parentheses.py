# Problem: 1021. Remove Outermost Parentheses
# LeetCode: https://leetcode.com/problems/remove-outermost-parentheses/
# Difficulty: Easy
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0
        for ch in s:
            if ch == '(':
                if count > 0:
                    res.append(ch)
                count += 1
            else:
                count -= 1
                if count > 0:
                    res.append(ch)
        return "".join(res)
