# Problem: 124. Binary Tree Maximum Path Sum
# LeetCode: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Difficulty: Hard
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            # Use max(0, ...) to ignore negative paths entirely
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            # Update the global maximum path sum including the split at current node
            res = max(res, left_sum + right_sum + node.val)

            # Return the maximum one-way gain for the parent caller
            return max(left_sum, right_sum) + node.val

        dfs(root)
        return res
