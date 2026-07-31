# Problem: 3016. Minimum Number of Pushes to Type Word II
# LeetCode: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
# Difficulty: Medium

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)

        ans = 0

        for i in range(26):
            if freq[i] == 0:
                break

            pushes = (i // 8) + 1

            ans += freq[i] * pushes

        return ans
