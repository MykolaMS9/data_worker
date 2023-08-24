SELECT s.fullname, gr.name, g.grade, g.date_of, d.name 
FROM students s 
JOIN [groups] gr ON s.group_id = gr.id 
JOIN grades g ON g.student_id  = s.id 
JOIN disciplines d ON d.id  = g.discipline_id 
WHERE gr.id  = 1 AND d.id = 1
ORDER BY g.date_of  ASC;