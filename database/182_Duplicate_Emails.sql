# Problem: 182. Duplicate Emails
# LeetCode: https://leetcode.com/problems/duplicate-emails/
# Difficulty: Easy

SELECT email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
