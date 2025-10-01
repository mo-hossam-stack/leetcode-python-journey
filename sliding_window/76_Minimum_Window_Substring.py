# Problem: Minimum Window Substring
# LeetCode: https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need =Counter(t)
        have =defaultdict(int)
        required= len(need)
        formed=0

        left=0
        res=(float("inf"), 0, 0)

        for right, ch in enumerate(s):
            have[ch] +=1

            if ch in need and have[ch] == need[ch]:
                formed+= 1

            while left <=right and formed == required:
                if right -left +1<res[0]:
                    res = (right-left + 1, left, right)

                have[s[left]]-=1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed-=1
                left+=1

        return "" if res[0]==float("inf")else s[res[1]:res[2]+1]