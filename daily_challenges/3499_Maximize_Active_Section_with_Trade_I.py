# Problem: 3499. Maximize Active Section with Trade I
# LeetCode: https://leetcode.com/problems/maximize-active-section-with-trade-i/
# Difficulty: Medium

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zeros = map(len, filter(None, s.split("1")))
        maxzeros = max(map(sum, pairwise(zeros)), default=0)
        return s.count("1") + maxzeros
