# Problem: 572. Subtree of Another Tree
# LeetCode: https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False

            if root1.val != root2.val: return False

            return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)

        def has_subtree(root):
            if not root: return False
            if same_tree(root, subRoot): return True

            return has_subtree(root.left) or has_subtree(root.right)

        return has_subtree(root)
