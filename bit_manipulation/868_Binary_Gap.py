# Problem: 868. Binary Gap
# LeetCode: https://leetcode.com/problems/binary-gap/
# Difficulty: Easy

class Solution(object):
    def binaryGap(self, N):
        A = [i for i in range(32) if (N >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in range(len(A) - 1))
