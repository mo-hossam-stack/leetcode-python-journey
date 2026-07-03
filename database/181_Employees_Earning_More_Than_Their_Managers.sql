# Problem: 181. Employees Earning More Than Their Managers
# LeetCode: https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Difficulty: Easy

SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary
