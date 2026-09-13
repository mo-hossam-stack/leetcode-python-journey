# Problem: 835. Image Overlap
# LeetCode: https://leetcode.com/problems/image-overlap/
# Difficulty: Medium
class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        frequency = {}
        maxOverlap = 0

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                dr = r1 - r2
                dc = c1 - c2

                key = (dr, dc)
                frequency[key] = frequency.get(key, 0) + 1
                maxOverlap = max(maxOverlap, frequency[key])

        return maxOverlap
