# Problem: 230. Kth Smallest Element in a BST
# LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None

        def inorder(node):
            if not node or self.res:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.res = node
                return
            inorder(node.right)

        inorder(root)
        return self.res.val
