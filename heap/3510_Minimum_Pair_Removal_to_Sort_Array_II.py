# Problem: Minimum Pair Removal to Sort Array II
# LeetCode: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
# Difficulty: Hard

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [i - 1  for i in range(n)]
        nxt = [i + 1  for i in range(n)]
        nxt[-1] = -1
        q = []
        unord = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                unord +=1
            heappush(q, (nums[i-1] + nums[i] , i))

        res = 0
        while unord !=0 :
            total ,r = heappop(q)
            l = prev[r]
            if l == -1 or nums[l] + nums[r] != total:
                continue
            nxt[l] = nxt[r]
            prev[nxt[r]] = l
            if nums[l] > nums[r]:
                unord -=1
            left = prev[l]
            right = nxt[r]
            if left !=-1:
                unord += (nums[left] > total) - (nums[left] > nums[l])
                heappush(q , (nums[left] + total , l))
            if right != -1:
                unord += (total > nums[right]) - (nums[r] > nums[right])
                heappush(q , (nums[right] + total , right))
            nums[l] = total
            nums[r] = inf
            res += 1
        return res
