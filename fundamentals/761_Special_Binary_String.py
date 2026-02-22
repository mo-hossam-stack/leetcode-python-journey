# Problem: 761. Special Binary String
# LeetCode: https://leetcode.com/problems/special-binary-string/
# Difficulty: Hard

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if s == '':
            return ''
        ans = []
        cnt = 0
        i = j = 0
        while i < len(s):
            cnt += 1 if s[i] == '1' else -1
            if cnt == 0:
                ans.append('1' + self.makeLargestSpecial(s[j + 1 : i]) + '0')
                j = i + 1
            i += 1

        ans.sort(reverse=True)
        return ''.join(ans)
