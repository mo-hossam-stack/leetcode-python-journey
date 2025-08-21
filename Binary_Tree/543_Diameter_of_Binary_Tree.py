# Problem: 543. Diameter of Binary Tree
# LeetCode: https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        diameter = 0
        max_height_disct = {}

        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                left_height = max_height_disct.pop(node.left) if node.left else 0
                right_height = max_height_disct.pop(node.right) if node.right else 0
                diameter = max(diameter, left_height + right_height)
                max_height_disct[node] = max(left_height, right_height) + 1
        
        return diameter
