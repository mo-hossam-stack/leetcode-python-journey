# Problem: Count Number of Trapezoids I
# LeetCode: https://leetcode.com/problems/count-number-of-trapezoids-i/
# Difficulty: Medium

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        freq_y = Counter(y for _,y in points)
        prefix_sum = res = 0
        MOD = 10**9 + 7
        for y in freq_y:

            comb = freq_y[y] * (freq_y[y] - 1) // 2

            res += prefix_sum * comb 
            prefix_sum += comb

        return res % MOD