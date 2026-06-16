# Problem: 176. Second Highest Salary
# LeetCode: https://leetcode.com/problems/second-highest-salary/
# Difficulty: Medium

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
