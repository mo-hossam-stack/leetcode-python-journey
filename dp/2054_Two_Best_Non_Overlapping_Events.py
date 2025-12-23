# Problem: Two Best Non-Overlapping Events
# LeetCode: https://leetcode.com/problems/two-best-non-overlapping-events/
# Difficulty: Medium

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def maxValue(E: List[List[int]], k: int) -> int:

            E.sort(key = lambda x: x[1]) # by END TIME... 

            @cache
            def dp(j, k_):
                return max(dp(j-1,k_), dp(bisect_left(E, E[j-1][0], key = lambda x: x[1]), k_-1) + E[j-1][2]) if j and k_ else 0


            return dp(len(E), k)

        return maxValue(events, 2)
