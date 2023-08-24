SELECT d.name as discipline, s.fullname as student_name, t.fullname as teacher_name
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id  
JOIN students s ON s.id = g.student_id 
JOIN teachers t  ON d.teacher_id  = t.id  
WHERE s.id = 1 AND t.id = 1
GROUP BY d.id 
ORDER BY d.id ASC;