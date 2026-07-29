# Problem: 606. Construct String from Binary Tree
# LeetCode: https://leetcode.com/problems/construct-string-from-binary-tree/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root):
        if root is None:
            return ""
        result = []

        self.preorderTraversal(root, result)

        return ''.join(result)

    def preorderTraversal(self, node, result):
        if node is None:
            return

        result.append(str(node.val))

        if node.left is not None or node.right is not None:

            result.append("(")
            self.preorderTraversal(node.left, result)
            result.append(")")

        if node.right is not None:
            result.append("(")
            self.preorderTraversal(node.right, result)
            result.append(")")
