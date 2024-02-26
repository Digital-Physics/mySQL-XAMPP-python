SELECT * 
FROM client
WHERE client_name LIKE '%LLC'; -- pattern ends with 'LLC''

SELECT *
FROM branch_suppplier
WHERE supplier_name LIKE '%Label%'; -- pattern containts 'Label'

SELECT *
FROM employee
WHERE birth_date LIKE '____-10%'; -- October birthdate

-- or
SELECT *
FROM employee
WHERE MONTH(birth_date) = 10;

-- UNION requires the same number of columns 
-- UNION requires the same data types
SELECT first_name AS various_names
FROM employee
UNION
SELECT branch_name
FROM branch
UNION
SELECT client_name
FROM client;

-- do some UNION ALL experiments with overlapping duplicate in the intersection
-- do some UNION ALL experiments with duplicate in one side. If we have two 'Marks' does the UNION keep them both, or is this a 'set' without duplicates.

-- speaking of duplicates, how would you identify and remove duplicates in sql?
WITH unique_cte AS (
  SELECT DISTINCT *
  FROM original_table
)

SELECT *
FROM unique_cte;

-- or
CREATE TABLE new_table AS
SELECT DISTINCT * FROM original_table;

-- a window function
-- COUNT(column) OVER (PARTITION BY column)
-- can use it to get the total COUNT/SUM/MAX of your class 
SELECT 
    first_name, 
    last_name, 
    sex, 
    salary,
    COUNT(sex) OVER (PARTITION BY sex) AS total_gender_counts 
FROM employee e
JOIN branch b ON e.emp_id = b.branch_id

-- alternatively
SELECT
    first_name,
    last_name,
    sex,
    salary
    subquery.sex_total AS total_gender_counts
FROM employee e
JOIN (SELECT sex, COUNT(sex) sex_total FROM employee GROUP BY sex) subquery
ON e.sex = subquery.sex
