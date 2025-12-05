# Problem: 2211 Count Collisions on a Road
# LeetCode: https://leetcode.com/problems/count-collisions-on-a-road/
# Difficulty: Medium

class Solution:
    def countCollisions(self, directions: str) -> int:
        return len(directions.lstrip('L').rstrip('R').replace('S',''))