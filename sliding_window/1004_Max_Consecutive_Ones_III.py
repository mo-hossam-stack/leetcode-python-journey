class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = num_zeros = l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros+=1
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l +=1
            max_len = max(max_len, r-l+1)
        return max_len