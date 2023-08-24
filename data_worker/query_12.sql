SELECT GROUP_CONCAT(s.fullname) as student_name, gr.name, d.name as discipline, GROUP_CONCAT(g.grade), g.date_of 
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id  
JOIN students s ON s.id = g.student_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 1 AND d.id = 1
GROUP BY g.date_of 
ORDER BY g.date_of  DESC
LIMIT 1;