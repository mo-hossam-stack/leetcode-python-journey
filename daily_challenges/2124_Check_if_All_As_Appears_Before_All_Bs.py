# Problem: 2124. Check if All A's Appears Before All B's
# LeetCode: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Difficulty: Easy
class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        l = -1
        for i in range(n - 1 , -1 , -1):
            if s[i] == 'a':
                l = i
                break
        if l == -1:
            return True
        
        for i in range(l):
            if s[i] == 'b':
                return False
        return True
