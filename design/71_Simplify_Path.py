# Problem: 71. Simplify Path
# LeetCode: https://leetcode.com/problems/simplify-path/
# Difficulty: Medium

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        components = path.split('/')
        
        for component in components:
            if component == "" or component == ".":
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        
        return "/" + "/".join(stack)
