SELECT  t.fullname, d.name
FROM disciplines d
JOIN teachers t ON d.teacher_id  = t.id 
--WHERE t.id  = 1
GROUP BY d.name 
ORDER BY t.fullname ASC;