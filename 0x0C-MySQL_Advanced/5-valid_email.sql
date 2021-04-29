-- Script that creates a trigger that resets an attribute

DELIMITER $$
CREATE TRIGGER validEmail
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email
        THEN
            SET NEW.valid_email = 0;
    END IF;
END;$$
DELIMITER;