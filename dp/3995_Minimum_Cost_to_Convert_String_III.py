# Problem: 3995. Minimum Cost to Convert String III
# LeetCode: https://leetcode.com/problems/minimum-cost-to-convert-string-iii/
# Difficulty: Hard

class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        prep = []
        for (p, r), base_cost in zip(rules, costs):
            w = p.count('*')
            total_cost = base_cost + w
            prep.append((p, r, total_cost, len(p)))
            
        vor = prep
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue
                
            if source[i] == target[i]:
                if dp[i] < dp[i + 1]:
                    dp[i + 1] = dp[i]
            
            for p, r, r_cost, le in vor:
                if i + le <= n:
                    if target[i : i + le] == r:
                        src_sub = source[i : i + le]
                        match = True
                        for p_char, s_char in zip(p, src_sub):
                            if p_char != '*' and p_char != s_char:
                                match = False
                                break
                        
                        if match:
                            if dp[i] + r_cost < dp[i + le]:
                                dp[i + le] = dp[i] + r_cost
                                
        return dp[n] if dp[n] != float('inf') else -1
