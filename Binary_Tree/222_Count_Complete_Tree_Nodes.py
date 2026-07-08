# Problem: 222. Count Complete Tree Nodes
# LeetCode: https://leetcode.com/problems/count-complete-tree-nodes/
# Difficulty: Easy

class Solution:
    def countNodes(self, n: Optional[TreeNode]) -> int:
        l, r, h = n, n, 0
        while l and r: 
            l, r, h = l.left, r.right, h + 1
        return 2**h - 1 if l == r else sum(map(self.countNodes, (n.left, n.right))) + 1
