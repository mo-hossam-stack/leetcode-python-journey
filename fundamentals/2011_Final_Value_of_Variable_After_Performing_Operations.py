# Problem: Final Value of Variable After Performing Operations
# LeetCode: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Difficulty: Easy

class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for operation in operations:
            if '+' in operation:
                x += 1
            else:
                x -= 1
        return x