# Problem: 144. Binary Tree Preorder Traversal
# LeetCode: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def preorder_helper(node):
            if not node:
                return
            result.append(node.val)
            preorder_helper(node.left)
            preorder_helper(node.right)

        preorder_helper(root)
        return result
