# Problem: Count and Say
# LeetCode: https://leetcode.com/problems/count-and-say/
# Difficulty: Medium

class Solution:
    def countAndSay(self, n: int) -> str:
        if n ==1:return "1"
        
        curr = "1"
        for _ in range(n-1):
            new_str = []
            count = 1
            for j in range(1, len(curr)):
                if curr[j]==curr[j - 1]:
                    count+= 1
                else:
                    new_str.append(f"{count}{curr[j - 1]}")
                    count = 1
            new_str.append(f"{count}{curr[-1]}")
            curr = "".join(new_str)
        
        return curr