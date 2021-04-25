-- CREATE DATABASE pp2demo;
-- CREATE USER pp2user with PASSWORD '123';
-- GRANT ALL PRIVILEGES ON DATABASE pp2demo TO pp2user;
-- DROP DATABASE pp2demo;
CREATE TABLE students (
    id VARCHAR(15),
    name VARCHAR(100),
    faculty VARCHAR(100),
    gpa NUMERIC
);
--Inserting data
INSERT INTO students (id, name, faculty, gpa)
VALUES ('19B030123', 'Zhaparov Nurlan', 'FIT', '2.90');

INSERT INTO students (id, name, faculty, gpa)
VALUES
       ('20B030123', 'Zhaparov Nurlan', 'FIT', '2.90'),
       ('21B030123', 'Zhaparov Nurlan', 'FIT', '2.90');

INSERt INTO students (id, name, faculty, gpa)
VALUES
      ('19B030111', 'Student 4', 'FEOGI', '3.50'),
      ('20B030555', 'Student 5', 'BS', '4.00');

SELECT id, name, faculty, gpa FROM students;
SELECT id, gpa FROM students;
-- Getting all the columns from the table
SELECT * from students;

-- filters
SELECT * FROM students
WHERE gpa >= 2.90;

SELECT * FROM students
WHERE gpa > 2.80 and faculty = 'FIT';

SELECT * FROM students ORDER BY gpa ASC;
SELECT * FROM students ORDER BY gpa DESC;

SELECT * FROM students
WHERE gpa > 2.80 and faculty = 'FIT'
ORDER BY id;

SELECT 2+5 * 10 - 4;
SELECT 10*10 AS result_of_multiplication;

-- LIKE means adding a pattern, starting with a letter Z for example
SELECT *
FROM students
WHERE name LIKE 'Z%';

SELECT * FROM students
WHERE name LIKE '%n';

SELECT * FROM students
WHERE name LIKE 'S%5';
-- kind of OR
SELECT * FROM students
WHERE id IN ('19B030123', '20B030555');
-- excluding
SELECT * FROM students
WHERE id NOT IN ('19B030123');
-- between
SELECT * FROM students
WHERE gpa BETWEEN 3.0 and 4;
-- updating
UPDATE students
SET faculty='BS'
WHERE id = '21B030123';
-- WHERE id IN ('21B030123, '19B030123);

SELECT * FROM students
WHERE gpa > 2.5
LIMIT 1;

-- DELETE FROM students WHERE id = '21B030123';
-- DELETE FROM students WHERE gpa > 3;

-- DDL and DML
-- Data Definition Language and Data Manipulation Language
-- DDL: CREATE db, table, user and so on
-- DML: INSERT, UPDATE, DELETE

