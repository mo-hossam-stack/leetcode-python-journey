# Problem: 183. Customers Who Never Order
# LeetCode: https://leetcode.com/problems/customers-who-never-order/
# Difficulty: Easy

SELECT name as Customers
from Customers
where id not in (
    select customerId
    from Orders
);
