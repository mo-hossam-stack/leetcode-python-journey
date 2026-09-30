# Problem: 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# LeetCode: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# Difficulty: Medium
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0] * len(seq)
        depth = 0
        for i, ch in enumerate(seq):
            if ch == '(':
                depth += 1
                ans[i] = depth % 2
            else:
                ans[i] = depth % 2
                depth -= 1
        return ans
