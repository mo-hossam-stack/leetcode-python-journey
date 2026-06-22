# Problem: 235. Lowest Common Ancestor of a Binary Search Tree
# LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root 

        while temp:
            if p.val > temp.val and q.val > temp.val:
                temp = temp.right
            elif p.val < temp.val and q.val < temp.val:
                temp = temp.left
            else:
                return temp
