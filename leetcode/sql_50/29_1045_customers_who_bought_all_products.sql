-- LeetCode SQL 50 #29
-- Problem 1045. Customers Who Bought All Products
-- Category: Sorting and Grouping
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
with num_freq as (
    select
        num, count(*) as freq
    from
        MyNumbers
    group by
        num
)

select
    max(num) as num
from
    num_freq
where
    freq = 1
