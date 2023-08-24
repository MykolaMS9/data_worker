SELECT s.fullname, gr.name 
FROM students s 
JOIN [groups] gr ON s.group_id = gr.id 
--WHERE gr.id  = 6
GROUP BY s.fullname  
ORDER BY gr.name ASC;