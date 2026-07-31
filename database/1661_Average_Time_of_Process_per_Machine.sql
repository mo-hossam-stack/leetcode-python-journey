-- Problem: 1661. Average Time of Process per Machine
-- LeetCode: https://leetcode.com/problems/average-time-of-process-per-machine/
-- Difficulty: Easy

SELECT A.machine_id, 
       ROUND(AVG(B.timestamp - A.timestamp), 3) AS processing_time
FROM Activity A
JOIN Activity B
ON A.machine_id = B.machine_id 
AND A.process_id = B.process_id
AND A.activity_type = 'start' 
AND B.activity_type = 'end'
GROUP BY A.machine_id;
