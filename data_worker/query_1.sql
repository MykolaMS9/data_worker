SELECT s.fullname, ROUND(AVG(g.grade), 2) AS avarage_grade  
FROM grades g 
JOIN students s ON s.id = g.student_id
GROUP BY s.fullname 
ORDER BY avarage_grade DESC 
LIMIT 5;