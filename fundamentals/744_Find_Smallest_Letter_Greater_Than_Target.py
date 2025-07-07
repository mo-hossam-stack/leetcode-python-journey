# Problem: Find Smallest Letter Greater Than Target
# LeetCode: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Difficulty: Easy

class Solution:
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
