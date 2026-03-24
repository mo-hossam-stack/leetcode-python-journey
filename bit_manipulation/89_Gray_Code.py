# Problem: 89. Gray Code
# LeetCode: https://leetcode.com/problems/gray-code/
# Difficulty: Medium

class Solution:
    def grayCode(self, n: int) -> List[int]:
        size = 1 << n
        return [i ^ (i >> 1) for i in range(size)]
