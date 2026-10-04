-- Write your query below
WITH RankedExams AS(
    SELECT student_id, exam_id, score, RANK() OVER (PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as rnk FROM exam_results
)
SELECT student_id, exam_id, score FROM RankedExams WHERE rnk=1