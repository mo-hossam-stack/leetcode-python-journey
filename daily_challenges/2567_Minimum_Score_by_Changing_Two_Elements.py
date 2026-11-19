# Problem: 2567. Minimum Score by Changing Two Elements
# LeetCode: https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Difficulty: Medium
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        small = nsmallest(3, nums)
        large = nlargest(3, nums)
        return min(large[0] - small[2], large[1] - small[1], large[2] - small[0])
