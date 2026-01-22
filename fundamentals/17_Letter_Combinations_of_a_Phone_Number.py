# Problem: Letter Combinations of a Phone Number
# LeetCode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty: Medium

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        hash_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        comb = []
        
        def try_comb(i):
            if i == len(digits):
                res.append("".join(comb))
                return
            for letter in hash_map[digits[i]]:
                comb.append(letter)
                try_comb(i + 1)
                comb.pop()
        
        try_comb(0)
        return res
