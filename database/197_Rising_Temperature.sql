# Problem: 197. Rising Temperature
# LeetCode: https://leetcode.com/problems/rising-temperature/
# Difficulty: Easy

SELECT today.id
FROM Weather yesterday 
CROSS JOIN Weather today

WHERE DATEDIFF(today.recordDate,yesterday.recordDate) = 1
    AND today.temperature > yesterday.temperature
;
