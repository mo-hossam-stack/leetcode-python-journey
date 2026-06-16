# Problem: 3612. Process String with Special Operations I
# LeetCode: https://leetcode.com/problems/process-string-with-special-operations-i/
# Difficulty: Medium

class Solution:
    def processStr(self, s: str) -> str:
        ans = ""

        for c in s:
            if 'a' <= c <= 'z':
                ans += c
            elif c == '*':
                if ans:
                    ans = ans[:-1]
            elif c == '#':
                ans += ans
            else:
                ans = ans[::-1]

        return ans
