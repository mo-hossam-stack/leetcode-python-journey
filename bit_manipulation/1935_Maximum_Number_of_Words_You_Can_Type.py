# Problem: Maximum Number of Words You Can Type
# LeetCode: https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# Difficulty: Easy

class Solution:
    def canBeTypedWords_(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = set(brokenLetters)
        res = 0
        for word in words:
            can_type = True
            for c in word:
                if c in broken:
                    can_type = False
                    break
            res += can_type
        return res

    # Bitmask solution
    def canBeTypedWords2(self, text: str, brokenLetters: str) -> int:
        def convert_to_bitmask(word: str) -> int:
            bitmask = [1 << (ord(c) - ord('a')) for c in word]
            return functools.reduce(lambda a, b: a | b, bitmask, 0)

        bitmask = convert_to_bitmask(brokenLetters)
        return sum(1 for word in text.split() if convert_to_bitmask(word) & bitmask == 0)