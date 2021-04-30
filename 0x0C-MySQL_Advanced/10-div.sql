-- Script that creates a function 

DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
BEGIN
    IF b == 0
        RETURN 0;
    END IF;

    RETURN a / b;
END;$$
DELIMITER;