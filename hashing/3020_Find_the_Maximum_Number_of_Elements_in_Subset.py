# Problem: 3020. Find the Maximum Number of Elements in Subset
# LeetCode: https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/
# Difficulty: Medium

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        M=31622
        freq=Counter(nums)
        ans=1
        if (f1:=freq[1])>0:
            ans=f1-((f1&1)==0)
            freq.pop(1)
        if ans>=9: return ans

        for x,f in freq.items():
            if x>M: continue
            cnt=0
            y=x
            while y<=M and freq[y]>=2:
                cnt+=2
                y*=y
            cnt+=(freq[y]>=1)*2-1
            ans=max(ans, cnt)
            if ans==9: break
        return ans
