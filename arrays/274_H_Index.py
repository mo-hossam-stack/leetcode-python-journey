# Problem: 274. H-Index
# LeetCode: https://leetcode.com/problems/h-index/
# Difficulty: Medium

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0
