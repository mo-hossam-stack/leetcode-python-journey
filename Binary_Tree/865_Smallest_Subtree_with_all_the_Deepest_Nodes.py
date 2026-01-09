# Problem: Smallest Subtree with all the Deepest Nodes
# LeetCode: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return 0, None
            l = dfs(node.left)
            r = dfs(node.right)

            if l[0] == r[0]: return l[0] + 1, node
            elif l[0] > r[0]: return l[0] + 1, l[1]
            else: return r[0] + 1, r[1]

        return dfs(root)[1]
