# Problem: 3474. Lexicographically Smallest Generated String
# LeetCode: https://leetcode.com/problems/lexicographically-smallest-generated-string/
# Difficulty: Hard

class Solution:
    def generateString(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        ans = ['?'] * (n + m - 1)
        
        for i, b in enumerate(s):
            if b != 'T':
                continue
            for j, c in enumerate(t):
                v = ans[i + j]
                if v != '?' and v != c:
                    return ""
                ans[i + j] = c
        
        old_ans = ans[:]
        ans = ['a' if c == '?' else c for c in ans]
        
        for i, b in enumerate(s):
            if b != 'F':
                continue
            if ''.join(ans[i: i + m]) != t:
                continue
            for j in range(i + m - 1, i - 1, -1):
                if old_ans[j] == '?':
                    ans[j] = 'b'
                    break
            else:
                return ""
        return ''.join(ans)
