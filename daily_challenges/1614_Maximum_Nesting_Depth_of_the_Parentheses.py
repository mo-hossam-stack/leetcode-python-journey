# Problem: 1614. Maximum Nesting Depth of the Parentheses
# LeetCode: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Difficulty: Easy
class Solution:
    def maxDepth(self, s):
        depth = 0
        r = 0
        for c in s:
            if c == ')':
                depth -= 1
                continue
            if c != '(':
                continue
            depth += 1
            if depth > r:
                r = depth
        return r
