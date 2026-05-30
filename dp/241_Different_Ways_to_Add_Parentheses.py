# Problem: 241. Different Ways to Add Parentheses
# LeetCode: https://leetcode.com/problems/different-ways-to-add-parentheses/
# Difficulty: Medium
class Solution:
    def __init__(self):
        self.map = {}
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.map:
            return self.map[expression]

        result = []

        for i in range(len(expression)):
            ch = expression[i]

            if ch in '*+-':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        if ch == '+':
                            result.append(l + r)
                        elif ch == '-':
                            result.append(l - r) 
                        elif ch == '*':
                            result.append(l * r)

        if not result:
            result.append(int(expression))

        self.map[expression] = result

        return result
