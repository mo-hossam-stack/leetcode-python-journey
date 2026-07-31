-- Problem: 1667. Fix Names in a Table
-- LeetCode: https://leetcode.com/problems/fix-names-in-a-table/
-- Difficulty: Easy

SELECT user_id,CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(name,2,length(name)))) AS name
FROM Users ORDER BY user_id;
