# Problem: Count the Number of Computer Unlocking Permutations
# LeetCode: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
# Difficulty: Medium

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        for i in range(1, n):
            if complexity[0] >= complexity[i]:return 0


        return factorial(n-1) % (10**9 + 7)
