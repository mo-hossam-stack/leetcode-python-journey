# Problem: 3534. Path Existence Queries in a Graph II
# LeetCode: https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
# Difficulty: Hard

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sortedNums = [(nums[i], i) for i in range(n)]
        sortedNums.sort()

        point = [0] * n
        for i in range(n):
            point[sortedNums[i][1]] = i

        up = [0] * (n + 1)

        j = 0
        for i in range(n):
            while j + 1 < n and sortedNums[j + 1][0] - sortedNums[i][0] <= maxDiff:
                j += 1
            if j < i:
                j = i
            up[i] = j

        temp = n
        k = 0
        while temp:
            k += 1
            temp //= 2

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n):
            dp[i][0] = up[i]

        for col in range(1, k):
            for i in range(n):
                dp[i][col] = dp[dp[i][col - 1]][col - 1]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            st = min(point[u], point[v])
            en = max(point[u], point[v])

            if up[st] == st:
                ans.append(-1)
                continue

            node = st
            step = 0

            for i in range(k - 1, -1, -1):
                if dp[node][i] < en:
                    node = dp[node][i]
                    step += 1 << i

            if up[node] < en:
                ans.append(-1)
            else:
                ans.append(step + 1)

        return ans
