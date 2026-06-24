-- LeetCode SQL 50 #09
-- Problem 197. Rising Temperature
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH maxTemperatures as (
    SELECT t1.id, t1.temperature, t2.temperature as maxPrevious
    FROM Weather as t1
    LEFT JOIN Weather as t2 ON t1.recordDate = ((t2.recordDate) + INTERVAL '1 DAY')
    -- GROUP BY t1.id, t1.temperature
)

SELECT t3.id as Id
FROM maxTemperatures as t3
WHERE t3.temperature > t3.maxPrevious
;
