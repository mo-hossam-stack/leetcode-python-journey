# Problem: 1291. Sequential Digits
# LeetCode: https://leetcode.com/problems/sequential-digits/
# Difficulty: Medium

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    res.append(num)
        res.sort()
        return res
