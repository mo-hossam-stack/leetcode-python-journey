# Problem: 2196. Create Binary Tree From Descriptions
# LeetCode: https://leetcode.com/problems/create-binary-tree-from-descriptions/
# Difficulty: Medium

class Solution:
    def createBinaryTree(self, A: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for x, y, is_left in A:
            if x not in nodes:
                nodes[x] = TreeNode(x)
            if y not in nodes:
                nodes[y] = TreeNode(y)
            if is_left:
                nodes[x].left = nodes[y]
            else:
                nodes[x].right = nodes[y]
            children.add(y)

        for x, node in nodes.items():
            if x not in children:
                return node
