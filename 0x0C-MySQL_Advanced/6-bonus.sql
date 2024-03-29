-- Script that creates a stored procedure that 
-- adds a new correction for a student.

DELIMITER $$
CREATE PROCEDURE AddBonus (
        IN user_id INT, 
        IN project_name VARCHAR(255),
        IN score INT)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name
    FROM DUAL
    WHERE project_name NOT IN (SELECT name FROM projects);

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;$$
DELIMITER;