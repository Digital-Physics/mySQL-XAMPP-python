-- https://youtu.be/HXV3zeQKqGY?si=cAtxMvDNdajMI9p3&t=12905
CREATE TABLE trigger_test (
    message VARCHAR(100)
);

-- this could be helpful for doing or logging things when events happen
DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES('added new employee');
    END$$
DELIMITER ;

-- ER diagrams (infographic of Database schema)