<# Problem: 2833. Furthest Point From Origin
# LeetCode: https://leetcode.com/problems/furthest-point-from-origin/
# Difficulty: Easy
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(sum((c=='R')-(c=='L') for c in moves))+moves.count('_')
