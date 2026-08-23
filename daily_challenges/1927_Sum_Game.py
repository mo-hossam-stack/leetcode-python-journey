# Problem: 1927. Sum Game
# LeetCode: https://leetcode.com/problems/sum-game/
# Difficulty: Medium
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        sumL = sumR = qL = qR = 0

        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    qL += 1
                else:
                    sumL += int(num[i])
            else:
                if num[i] == '?':
                    qR += 1
                else:
                    sumR += int(num[i])

        if qL + qR == 0:
            return sumL != sumR

        if (qL + qR) % 2:
            return True

        if qL == qR:
            return sumL != sumR

        return 2 * (sumL - sumR) != 9 * (qR - qL)
