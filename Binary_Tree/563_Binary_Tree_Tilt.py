# Problem: 563. Binary Tree Tilt
# LeetCode: https://leetcode.com/problems/binary-tree-tilt/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTilt(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            self.ans += abs(left_sum - right_sum)

            return left_sum + right_sum + node.val

        dfs(root)
        return self.ans
