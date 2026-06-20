# Problem: 178. Rank Scores
# LeetCode: https://leetcode.com/problems/rank-scores/
# Difficulty: Medium

SELECT S.score ,COUNT(S2.SCORE) as `rank` FROM SCORES S,
(SELECT DISTINCT SCORE FROM SCORES)  S2
WHERE S.SCORE<=S2.SCORE 
GROUP BY S.ID 
ORDER BY S.SCORE DESC;
