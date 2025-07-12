# Problem: Removing Stars From a String
# LeetCode: https://leetcode.com/problems/removing-stars-from-a-string/
# Difficulty: Medium

class Solution:
    def removeStars(self, s):
        stack = []
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)