# Problem: 1415. The k-th Lexicographical String of All Happy Strings of Length n
# LeetCode: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
# Difficulty: Medium

class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        k -= 1
        result = []
        last = ""

        for pos in range(n):

            branch = 2 ** (n - pos - 1)
            choices = [c for c in "abc" if c != last]

            idx = k // branch
            result.append(choices[idx])

            last = choices[idx]
            k %= branch

        return "".join(result)
