# Problem: 113. Path Sum II
# LeetCode: https://leetcode.com/problems/path-sum-ii/
# Difficulty: Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, path, curSum):
            if not node: return
            curSum += node.val
            path.append(node.val)
            if not node.left and not node.right and curSum == targetSum:
                res.append(path[:])
            dfs(node.left, path, curSum)
            dfs(node.right, path, curSum)
            path.pop()
        dfs(root, [], 0)
        return res
