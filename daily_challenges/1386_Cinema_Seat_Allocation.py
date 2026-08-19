# Problem: 1386. Cinema Seat Allocation
# LeetCode: https://leetcode.com/problems/cinema-seat-allocation/
# Difficulty: Medium
class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for r, seat in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << seat)

        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        answer = (n - len(rows)) * 2

        for mask in rows.values():
            can_left = (mask & left) == 0
            can_middle = (mask & middle) == 0
            can_right = (mask & right) == 0

            if can_left and can_right:
                answer += 2
            elif can_left or can_middle or can_right:
                answer += 1

        return answer
