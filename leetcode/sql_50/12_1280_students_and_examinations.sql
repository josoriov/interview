-- LeetCode SQL 50 #12
-- Problem 1280. Students and Examinations
-- Category: Basic Joins
--
-- TODO:
-- - Summarize the main query idea.
-- - Note any filters, joins, or edge cases.
--
# Write your MySQL query statement below
WITH student_exams as (
    SELECT *
    FROM Students
    CROSS JOIN Subjects
), exam_attendance AS (
    SELECT student_id, subject_name, COUNT(1) AS total_attendance
    FROM Examinations
    GROUP BY student_id, subject_name
)

SELECT t1.student_id, t1.student_name, t1.subject_name, COALESCE(t2.total_attendance, 0) AS attended_exams
FROM student_exams as t1
LEFT JOIN exam_attendance as t2 ON t1.student_id = t2.student_id AND t1.subject_name = t2.subject_name
ORDER BY t1.student_id, t1.subject_name
;
