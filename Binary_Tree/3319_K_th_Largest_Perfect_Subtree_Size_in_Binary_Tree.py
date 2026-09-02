# Problem: 3319. K-th Largest Perfect Subtree Size in Binary Tree
# LeetCode: https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/
# Difficulty: Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):

            if not node:return 0

            left, rght = dfs(node.left), dfs(node.right)
            
            if left != rght: return -1
            
            ans.append(left + rght + 1)
            return left + rght + 1
            

        ans = []    
        dfs(root)

        if len(ans) < k: return -1
        return nlargest(k,ans)[k-1]
