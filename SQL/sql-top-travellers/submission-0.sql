-- Write your query below
SELECT name, COALESCE(SUM(rides.distance), 0) 
as travelled_distance FROM users LEFT JOIN rides on users.id=rides.user_id GROUP BY name ORDER BY travelled_distance DESC, name ASC;