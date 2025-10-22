# Problem: Maximum Number of Events That Can Be Attended II
# LeetCode: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
# Difficulty: Hard

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        starts = [s for s, _, _ in events]

        @cache
        def dp(i, count):
            if i == n or count == 0:
                return 0
            next = bisect_right(starts, events[i][1])
            return max(dp(i + 1, count), dp(next, count - 1) + events[i][2])

        return dp(0, k)