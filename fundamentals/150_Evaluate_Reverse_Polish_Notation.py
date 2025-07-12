# Problem: Evaluate Reverse Polish Notation
# LeetCode: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '*':
                    stack.append(a * b)
                elif char == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(char))
        return stack[0]