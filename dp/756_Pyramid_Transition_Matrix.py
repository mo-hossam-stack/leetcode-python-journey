# Problem: Pyramid Transition Matrix
# LeetCode: https://leetcode.com/problems/pyramid-transition-matrix/
# Difficulty: Medium

class Solution:
    def pyramidTransition(self, bottom, allowed):
        import collections, itertools
        from functools import cache

        f = collections.defaultdict(lambda: collections.defaultdict(list))
        for a, b, c in allowed:
            f[a][b].append(c)

        @cache
        def pyramid(cur):
            if len(cur) == 1:
                return True
            return any(
                pyramid(next_row)
                for next_row in itertools.product(
                    *(f[a][b] for a, b in zip(cur, cur[1:]))
                )
            )

        return pyramid(bottom)
