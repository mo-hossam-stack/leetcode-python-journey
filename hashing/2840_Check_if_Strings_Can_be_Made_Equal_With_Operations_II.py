# Problem: 2840. Check if Strings Can be Made Equal With Operations II
# LeetCode: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
# Difficulty: Medium

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(
            s1[1::2]
        ) == Counter(s2[1::2])
