-- Write your query below
SELECT left_operand, operator, right_operand, 
CASE 
    WHEN operator='>' THEN v1.value > v2.value
    WHEN operator='<' THEN v1.value < v2.value
    ELSE v1.value=v2.value
END AS value
FROM expressions
LEFT JOIN variables v1 ON left_operand=v1.name
LEFT JOIN variables v2 ON right_operand=v2.name
