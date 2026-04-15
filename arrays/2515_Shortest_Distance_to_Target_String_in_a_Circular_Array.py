# Problem: 2515. Shortest Distance to Target String in a Circular Array
# LeetCode: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
# Difficulty: Easy

class Solution:
    def closestTarget(
        self, words: List[str], target: str, startIndex: int
    ) -> int:
        ans = n = len(words)
        for i, word in enumerate(words):
            if word == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
        return ans if ans < n else -1
