-- Write your query below
SELECT s.name
FROM sales_person s
WHERE 
(SELECT com_id FROM company WHERE name='CRIMSON') NOT IN (SELECT orders.com_id FROM orders WHERE orders.sales_id=s.sales_id)