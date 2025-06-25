# Problem: Valid Parentheses
# LeetCode: https://leetcode.com/problems/valid-parentheses/description/
# Difficulty: Easy


class Solution:
    def arePair(self, open_, close):
        pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
        return pairs.get(open_) == close
    
    def isValid(self, exp: str) -> bool:
        stack = []
        for ch in exp:
            if ch in '([{<':
                stack.append(ch)
            elif ch in ')]}>':
                if not stack or not self.arePair(stack[-1], ch):
                    return False
                stack.pop()
        return not stack