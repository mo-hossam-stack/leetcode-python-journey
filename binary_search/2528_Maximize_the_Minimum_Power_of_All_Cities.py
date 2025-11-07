# Problem: Maximize the Minimum Power of All Cities
# LeetCode: https://leetcode.com/problems/maximize-the-minimum-powered-city/
# Difficulty: Hard

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        left = 0
        right = sum(stations) + k
        n = len(stations)

        def check(p):
            A = stations[:]
            num_additional_stations = k
            window_sum = sum(A[:min(n, r+1)])
            for i in range(n):
                if window_sum <p:
                    need = p -window_sum
                    num_additional_stations -= need
                    window_sum+= need
                    A[min(n-1, i+r)] += need
                if i-r >= 0:
                    window_sum -= A[i-r]
                if i+r+1 <n:
                    window_sum+= A[i+r+1]
            return num_additional_stations >= 0

        while left < right:
            m = ceil(left +(right - left) / 2)
            if check(m):
                left=m
            else:
                right=m - 1
        return left