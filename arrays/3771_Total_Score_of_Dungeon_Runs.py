# Problem: Total Score of Dungeon Runs
# LeetCode: https://leetcode.com/problems/total-score-of-dungeon-runs/
# Difficulty: Medium

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        # if we start with hp health at index i:

        # hp - damage[i] >= req[i]

        # hp - damage[i] - damage[i+1] >= req[i+1]
        # ...
        # hp - SUM damage[j] for j in range(i, n) >= req[n-1]
        # if we start with hp - damage[0] - damage[1] ... - damage[i]
        # hp - damage[1] ... - damage[i]
        # so at a given index i: just check for all hp - SUM_{j : k to i} damage[j] >= req[i]
        # where k varies from 0 to i...
        # note this is a mono decreasing sequence.
        # so we can binary search for the point that it is < req[i].
        n = len(damage)
        PS = list(accumulate(damage)) + [0]

        def check(i, k):
            return hp - (PS[i] - PS[k-1]) >= requirement[i]

        def count(i):
            l,r = 0, i
            while l < r:
                m = l + (r-l)//2
                if check(i, m):
                    r = m
                else:
                    l = m + 1
            return l

        res = 0
        for i in range(n):
            if check(i, i) == True:
                res += i - count(i) + 1
            # if all F, res += 0

        return res