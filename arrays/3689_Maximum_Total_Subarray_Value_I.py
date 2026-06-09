# Problem: 3689. Maximum Total Subarray Value I
# LeetCode: https://leetcode.com/problems/maximum-total-subarray-value-i/
# Difficulty: Medium

class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        return (max(A) - min(A)) * k
