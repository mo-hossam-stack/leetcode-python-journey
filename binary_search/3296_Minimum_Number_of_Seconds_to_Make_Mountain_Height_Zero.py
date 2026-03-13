# Problem: 3296. Minimum Number of Seconds to Make Mountain Height Zero
# LeetCode: https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/
# Difficulty: Medium


class Solution:
    def minNumberOfSeconds(self, height: int, times: list[int]) -> int:
        lo, hi = 1, 10**16

        while lo < hi:
            mid = (lo + hi) >> 1
            tot = 0
            for t in times:
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                if tot >= height: 
                    break
            
            if tot >= height:
                hi = mid
            else:
                lo = mid + 1

        return lo
