# Problem: 177. Nth Highest Salary
# LeetCode: https://leetcode.com/problems/nth-highest-salary/
# Difficulty: Medium

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END
