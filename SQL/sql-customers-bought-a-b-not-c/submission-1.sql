-- Write your query below
SELECT c.customer_id, c.customer_name FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE c.customer_id=o.customer_id AND o.product_name='A') AND
EXISTS (SELECT 1 FROM orders o WHERE c.customer_id=o.customer_id AND o.product_name='B') AND
NOT EXISTS (SELECT 1 FROM orders o WHERE c.customer_id=o.customer_id AND o.product_name='C') ORDER BY customer_name