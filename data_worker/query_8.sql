SELECT d.name, ROUND(AVG( g.grade), 2), t.fullname 
FROM disciplines d
JOIN grades g ON g.discipline_id  = d.id  
JOIN teachers t ON t.id  = d.teacher_id 
WHERE t.id = 5
GROUP BY d.name 
ORDER BY d.id  ASC;