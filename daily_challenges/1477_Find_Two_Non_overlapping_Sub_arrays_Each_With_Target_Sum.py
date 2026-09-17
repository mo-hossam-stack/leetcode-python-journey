# Problem: 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
# LeetCode: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
# Difficulty: Medium
class Solution:
    def minSumOfLengths(self, A: List[int], k: int) -> int:
        n = len(A)
        res, tot, i = n + 1, 0, 0

        dp = [n] * (n + 1)

        for j in range(n):
            tot += A[j]

            while tot > k:
                tot -= A[i]
                i += 1
                
            dp[j + 1] = dp[j]

            if tot == k:
                Len = j - i + 1

                res = min(res, Len + dp[i])
                dp[j + 1] = min(dp[j], Len)
            
        return -1 if res == n + 1 else res
