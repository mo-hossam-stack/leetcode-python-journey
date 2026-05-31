# Problem: 205. Isomorphic Strings
# LeetCode: https://leetcode.com/problems/isomorphic-strings/
# Difficulty: Easy
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i

            if t[i] not in char_index_t:
                char_index_t[t[i]] = i
            
            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        return True
