# Problem: 297. Serialize and Deserialize Binary Tree
# LeetCode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Difficulty: Hard

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root: return "null"
        res, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ','.join(res)

    def deserialize(self, data):
        if data == "null": return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            curr = q.popleft()
            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
