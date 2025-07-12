# Problem: Determine if String Halves Are Alike
# LeetCode: https://leetcode.com/problems/determine-if-string-halves-are-alike/
# Difficulty: Easy

class Solution:
    def halvesAreAlike(self, s):
        vowels = set('aeiouAEIOU')
        half = len(s) // 2
        count_a = count_b = 0

        for i in range(half):
            if s[i] in vowels:
                count_a += 1
            if s[i + half] in vowels:
                count_b += 1

        return count_a == count_b