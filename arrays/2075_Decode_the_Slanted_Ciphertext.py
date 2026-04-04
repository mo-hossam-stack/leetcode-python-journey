# Problem: 2075. Decode the Slanted Ciphertext
# LeetCode: https://leetcode.com/problems/decode-the-slanted-ciphertext/
# Difficulty: Medium

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows
        res = []

        for c in range(cols):
            r, j = 0, c
            while r < rows and j < cols:
                res.append(encodedText[r * cols + j])
                r += 1
                j += 1

        return "".join(res).rstrip()
