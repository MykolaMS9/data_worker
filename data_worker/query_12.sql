SELECT s.fullname as student_name, gr.name, d.name as discipline, g.grade, g.date_of 
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id  
JOIN students s ON s.id = g.student_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 5 AND d.id = 1
ORDER BY g.date_of  DESC;