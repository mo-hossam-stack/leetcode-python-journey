# Problem: 98. Validate Binary Search Tree
# LeetCode: https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
                return False
            
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        
        return valid(root, float("-inf"), float("inf"))
