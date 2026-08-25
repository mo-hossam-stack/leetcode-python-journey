-- Problem: 1393. Capital Gain/Loss
-- LeetCode: https://leetcode.com/problems/capital-gain-loss/
-- Difficulty: Medium
SELECT stock_name,  SUM(IF(operation='buy',-price,price)) as capital_gain_loss
from  Stocks
group by stock_name
