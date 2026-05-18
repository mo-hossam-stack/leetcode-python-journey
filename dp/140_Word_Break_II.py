# Problem: 140. Word Break II
# LeetCode: https://leetcode.com/problems/word-break-ii/
# Difficulty: Hard
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        @cache
        def dfs(start):
            if start == n: 
                return [""]
            
            ans=[]
            for w in wordDict:
                sz = len(w)
                if start+sz <=n and s[start:start+sz] == w:
                    rest = dfs(start + sz)
                    for r in rest:
                        if r == "": 
                            ans.append(w)
                        else: 
                            ans.append(w+" "+r)
            return ans
        
        return dfs(0)
