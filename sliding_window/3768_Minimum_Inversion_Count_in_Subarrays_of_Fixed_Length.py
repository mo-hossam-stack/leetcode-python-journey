# Problem: Minimum Inversion Count in Subarrays of Fixed Length
# LeetCode: https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/
# Difficulty: Hard

class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)
    
    def update(self, i, val):
        i += self.n
        self.tree[i] += val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
    
    def query(self, l, r):  # [l, r)
        res = 0
        l += self.n
        r +=self.n
        while l<r:
            if l&1:
                res +=self.tree[l]
                l+=1
            if r& 1:
                r-= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

class Solution:
    # for fixed index i: nums[i]. we know how many nums[j] < nums[i] there are for j in [i+1, i+k-1]
    # (seg tree) 
    # 
    # its just fixed sliding window.. use seg tree for updates... 
    def minInversionCount(self, nums: List[int], k: int) -> int:
        if k==1:return 0

        rank = {num :i for i,num in enumerate(sorted(set(nums)))}
        N = len(rank)
        st = SegTree(N)
        # idx are numbers 
        # values are the frequency count of that number
        n = len(nums)
        window_inversion_count = 0
        for i in range(k):
            window_inversion_count += st.query(rank[nums[i]] + 1, N)
            st.update(rank[nums[i]], 1)
        
        res = window_inversion_count
        # print(res)

        for i in range(n-k):
            # remove i
            # so all inversions that involve that i are gone...
            window_inversion_count -= st.query(0, rank[nums[i]])
            st.update(rank[nums[i]], -1)
            # print(window_inversion_count, res)
            # add the ones that involve nums[i+k-1]
            st.update(rank[nums[i+k]], +1)
            window_inversion_count += st.query(rank[nums[i+k]] + 1, N)
            res = min(res, window_inversion_count)
        return res
