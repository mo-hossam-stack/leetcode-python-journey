# Problem: 3525. Find X Value of Array II
# LeetCode: https://leetcode.com/problems/find-x-value-of-array-ii/
# Difficulty: Hard
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        size = 1
        while size < n:
            size <<= 1

        H = [0] * (2 * size * k)
        prod = [1 % k] * (2 * size)

        for i in range(n):
            v = nums[i] % k
            nd = size + i
            H[nd * k + v] = 1
            prod[nd] = v

        for i in range(size - 1, 0, -1):
            lc = 2 * i
            rc = lc + 1
            lp = prod[lc]

            bi = i * k
            bl = lc * k
            br = rc * k

            for q in range(k):
                H[bi + q] = H[bl + q]

            for q in range(k):
                c = H[br + q]
                if c:
                    H[bi + (lp * q) % k] += c

            prod[i] = lp * prod[rc] % k

        def update(idx: int, val: int) -> None:
            nd = size + idx
            base = nd * k

            for q in range(k):
                H[base + q] = 0

            v = val % k
            H[base + v] = 1
            prod[nd] = v

            i = nd >> 1

            while i:
                lc = 2 * i
                rc = lc + 1
                lp = prod[lc]

                bi = i * k
                bl = lc * k
                br = rc * k

                for q in range(k):
                    H[bi + q] = H[bl + q]

                for q in range(k):
                    c = H[br + q]
                    if c:
                        H[bi + (lp * q) % k] += c

                prod[i] = lp * prod[rc] % k
                i >>= 1

        ans = []

        for idx, val, start, x in queries:
            update(idx, val)

            l = start + size
            r = n + size

            ln = []
            rn = []

            while l < r:
                if l & 1:
                    ln.append(l)
                    l += 1

                if r & 1:
                    r -= 1
                    rn.append(r)

                l >>= 1
                r >>= 1

            rn.reverse()

            res = [0] * k
            p = 1 % k

            for nd in ln:
                base = nd * k

                for q in range(k):
                    c = H[base + q]
                    if c:
                        res[(p * q) % k] += c

                p = p * prod[nd] % k

            for nd in rn:
                base = nd * k

                for q in range(k):
                    c = H[base + q]
                    if c:
                        res[(p * q) % k] += c

                p = p * prod[nd] % k

            ans.append(res[x])

        return ans
