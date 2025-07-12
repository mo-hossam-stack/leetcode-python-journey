# Problem: Get Equal Substrings Within Budget
# LeetCode: https://leetcode.com/problems/get-equal-substrings-within-budget/
# Difficulty: Medium

class Solution:
    def equalSubstring(self, s, t, maxCost):
        left = 0
        cost = 0
        max_len = 0

        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))

            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len