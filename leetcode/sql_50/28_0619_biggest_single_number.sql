-- LeetCode SQL 50 #28
-- Problem 619. Biggest Single Number
-- Category: Sorting and Grouping
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
select
    user_id, count(follower_id) as followers_count
from
    Followers
group by
    user_id
order by
    user_id asc