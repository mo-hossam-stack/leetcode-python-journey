# Problem: 3723. Maximize Sum of Squares of Digits
# LeetCode: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
# Difficulty: Medium
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum:
            return ""
        
        curr = 0
        ans = ""
        while sum > 9:
            ans += "9"
            curr += 1
            sum -= 9
        if curr > num:
            return ""
        if num:
            ans += str(sum)
            curr += 1
        while curr < num:
            ans += "0"
            curr += 1
        return ans
