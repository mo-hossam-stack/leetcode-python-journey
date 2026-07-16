-- Problem: 602. Friend Requests II: Who Has the Most Friends
-- LeetCode: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Difficulty: Medium

WITH ids AS (
    SELECT
        requester_id AS id
    FROM 
        RequestAccepted

    UNION ALL

    SELECT
        accepter_id AS id
    FROM 
        RequestAccepted
)

SELECT
    id,
    COUNT(id) AS num
FROM ids
GROUP BY
    id
ORDER BY
    num DESC
LIMIT 1;
