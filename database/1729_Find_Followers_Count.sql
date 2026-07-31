-- Problem: 1729. Find Followers Count
-- LeetCode: https://leetcode.com/problems/find-followers-count/
-- Difficulty: Easy

select user_id, 
    count(distinct follower_id) as followers_count
from followers
group by user_id;
