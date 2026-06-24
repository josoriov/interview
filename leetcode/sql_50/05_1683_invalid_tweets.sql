-- LeetCode SQL 50 #05
-- Problem 1683. Invalid Tweets
-- Category: Select
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
select t1.tweet_id
from Tweets as t1
where substring(t1.content, 1, 15) <> t1.content;
