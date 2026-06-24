-- LeetCode SQL 50 #10
-- Problem 1661. Average Time of Process per Machine
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
-- Write your PostgreSQL query statement below
WITH process_starts AS (
    SELECT t1.machine_id, t1.process_id, t1.timestamp as timestamp_start
    FROM Activity as t1
    WHERE t1.activity_type = 'start'
), process_ends AS (
    SELECT t2.machine_id, t2.process_id, t2.timestamp as timestamp_end
    FROM Activity as t2
    WHERE t2.activity_type = 'end'
)

SELECT t3.machine_id, ROUND(AVG(t4.timestamp_end - t3.timestamp_start)::numeric, 3) as processing_time
FROM process_starts as t3
LEFT JOIN process_ends as t4 ON t3.machine_id = t4.machine_id and t3.process_id = t4.process_id
GROUP BY t3.machine_id
;
