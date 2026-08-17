# Problem: 1563. Stone Game V
# LeetCode: https://leetcode.com/problems/stone-game-v/
# Difficulty: Hard
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        for left in range(n - 1, -1, -1):
            mid = left - 1
            leftSum = 0
            totalSum = stoneValue[left]

            for right in range(left + 1, n):
                totalSum += stoneValue[right]

                while mid + 1 < right and (leftSum + stoneValue[mid + 1]) * 2 <= totalSum:
                    mid += 1
                    leftSum += stoneValue[mid]

                res = 0

                if mid >= left and leftSum * 2 == totalSum:
                    res = max(maxL[left][mid], maxR[mid + 1][right])
                else:
                    if mid >= left:
                        res = maxL[left][mid]
                    if mid + 1 < right:
                        res = max(res, maxR[mid + 2][right])

                dp[left][right] = res

                maxL[left][right] = max(maxL[left][right - 1], totalSum + res)
                maxR[left][right] = max(maxR[left + 1][right], totalSum + res)

        return dp[0][n - 1]
