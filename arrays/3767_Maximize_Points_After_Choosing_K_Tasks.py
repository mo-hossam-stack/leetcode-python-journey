#Problem: Maximize Points After Choosing K Tasks
#LeetCode: https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/description/
#Difficulty: Medium

class Solution:
    # clearly choose all the ones where technique 1 > tech 2
    # but if that is less than k, you just take the CLOSEST ones lower.
    def maxPoints(self, A: List[int], B: List[int], k: int) -> int:
        n = len(A)
        taken = set()
        res = 0
        for i in range(n):
            if A[i] > B[i]:

                taken.add(i)
                res += A[i]

        if len(taken) < k:
            rest = [(B[i] - A[i], A[i], i) for i in range(n) if i not in taken]

            rest.sort()

            for idx in range(k - len(taken)):
                _, a, i = rest[idx]
                res += a
                taken.add(i)

        for i in range(n):
            if i not in taken:

                res += B[i]
        return res
