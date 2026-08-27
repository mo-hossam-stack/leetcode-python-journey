# Problem: 3720. Lexicographically Smallest Permutation Greater Than Target
# LeetCode: https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/
# Difficulty: Medium
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for i in range(n - 1, -1, -1):

            remain = cnt[:]

            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if remain[x] == 0:
                    possible = False
                    break

                remain[x] -= 1

            if not possible:
                continue
            target_char = ord(target[i]) - ord('a')

            for c in range(target_char + 1, 26):

                if remain[c] == 0:
                    continue

                ans = target[:i]

                ans += chr(ord('a') + c)

                remain[c] -= 1

                for x in range(26):
                    ans += chr(ord('a') + x) * remain[x]

                return ans

        return ""
