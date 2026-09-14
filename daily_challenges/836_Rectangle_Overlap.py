# Problem: 836. Rectangle Overlap
# LeetCode: https://leetcode.com/problems/rectangle-overlap/
# Difficulty: Easy
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])

        bottom = max(rec1[1], rec2[1])
        top = min(rec1[3], rec2[3])

        return left < right and bottom < top
