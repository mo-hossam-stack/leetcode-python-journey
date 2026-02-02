# Problem: 44. Wildcard Matching
# LeetCode: https://leetcode.com/problems/wildcard-matching/
# Difficulty: Hard

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si, pi, match, star = 0, 0, 0, -1
        sn, pn = len(s), len(p)
        while si < sn:
            if pi < pn and (p[pi] == '?' or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < pn and p[pi] == '*':
                star = pi
                match = si
                pi += 1
            elif star != -1:
                pi = star + 1
                match += 1
                si = match
            else:
                return False
        while pi < pn and p[pi] == '*':
            pi += 1
        return pi == pn
