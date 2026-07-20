# Problem: 748. Shortest Completing Word
# LeetCode: https://leetcode.com/problems/shortest-completing-word/
# Difficulty: Easy

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_chars = [char.lower() for char in licensePlate if char.isalpha()]
        license_count = Counter(license_chars)
        
        words.sort(key=len)

        for word in words:
            word_count = Counter(word)
            if all(word_count[char] >= license_count[char] for char in license_count):
                return word
