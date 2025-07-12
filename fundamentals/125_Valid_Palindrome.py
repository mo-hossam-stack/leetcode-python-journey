class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = ""
        for char in s:
            if char.isalnum():
                ret += char
        ret = ret.lower()
        return ret[:] == ret[::-1]