# Problem: Container With Most Water
# LeetCode: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            hi = min(height[left], height[right])
            wid = right - left
            curr_area = wid * hi
            max_area = max(max_area, curr_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
