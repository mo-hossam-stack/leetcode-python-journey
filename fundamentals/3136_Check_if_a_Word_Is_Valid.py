# Problem: Check if a Word Is Valid
# LeetCode: https://leetcode.com/problems/check-if-a-word-is-valid/
# Difficulty: Easy

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = 'aeiou'
        vowels += vowels.upper()
        consonants = 'qwrtyplkjhgfdszxcvbnm'
        consonants += consonants.upper()
        allowed = consonants + vowels + '0123456789'
        f_vowels = f_consonants = False
        for c in word:
            if c in vowels:
                f_vowels = True
            if c in consonants:
                f_consonants = True
            if c not in allowed:
                return False
        return f_vowels and f_consonants