# Problem: 180. Consecutive Numbers
# LeetCode: https://leetcode.com/problems/consecutive-numbers/
# Difficulty: Medium

with cte as (
    select num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    from logs

)

select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2)
