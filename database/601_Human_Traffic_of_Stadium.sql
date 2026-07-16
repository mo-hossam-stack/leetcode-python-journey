-- Problem: 601. Human Traffic of Stadium
-- LeetCode: https://leetcode.com/problems/human-traffic-of-stadium/
-- Difficulty: Hard

with Segmented as (
    select *, 
        id - row_number() over (order by id) as island_id
    from Stadium
    where people >= 100
)
select id, visit_date, people
from Segmented
where island_id in (select island_id
                    from Segmented
                    group by island_id
                    having count(*) >= 3)
