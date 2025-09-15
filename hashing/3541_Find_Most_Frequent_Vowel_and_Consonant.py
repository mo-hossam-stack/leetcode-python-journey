# Problem: Find Most Frequent Vowel and Consonant
# LeetCode: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
# Difficulty: Easy

from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s)
        vowels = 'aeiou'
        max_vowel_freq = max((f for c, f in freq.items() if c in vowels), default=0)
        max_consonant_freq = max((f for c, f in freq.items() if c not in vowels), default=0)
        return max_vowel_freq + max_consonant_freq