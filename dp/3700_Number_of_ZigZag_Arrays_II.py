# Problem: 3700. Number of ZigZag Arrays II
# LeetCode: https://leetcode.com/problems/number-of-zigzag-arrays-ii/
# Difficulty: Hard

MOD = 10**9 + 7

class Matrix(list):
    def __matmul__(A, B):
        C = [[0] * len(B[0]) for _ in A]
        for i, row in enumerate(A):
            for k, v in enumerate(row):
                C[i] = [(c + v * b) % MOD for c, b in zip(C[i], B[k])]
        return Matrix(C)

    def __pow__(A, e: int):
        n = len(A)
        ans = Matrix([[+(i == j) for j in range(n)] for i in range(n)])
        base = A
        while e:
            if e & 1:
                ans = ans @ base
            base = base @ base
            e >>= 1
        return ans

class Solution:
    def zigZagArrays(self, N, L, R):
        K = R - L + 1

        M1 = Matrix([[+(i < j) for j in range(K)] for i in range(K)])
        M2 = Matrix([[K - 1 - max(i, j) for j in range(K)] for i in range(K)])

        pairs, rem = divmod(N - 1, 2)
        A = M2 ** pairs
        if rem:
            A = A @ M1

        return sum(sum(row) for row in A) * 2 % MOD
