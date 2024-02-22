from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
engine = create_engine(f"mysql+pymysql://{env_vars['APP_USER']}:{env_vars['PASSWORD']}@{env_vars['HOST']}:{env_vars['DB_PORT']}/{env_vars['DATABASE']}")
Session = sessionmaker(bind=engine)
session = Session()

sql_query = """
SELECT * FROM city
WHERE countryCode = 'USA' 
AND population > 100000 
"""

sql_query = """
SELECT name FROM city
WHERE countryCode = 'USA' 
AND population > 120000 
"""

"""
SELECT * FROM city
WHERE id = 1661
"""

"""
SELECT * FROM city
WHERE id = 1661
"""

"""
SELECT name FROM city
WHERE countryCode = 'JPN' 
"""

"""
select city, state from station
"""

"""
select city from station
where id % 2 = 0 
group by city
"""

"""
SELECT COUNT(*) - COUNT(DISTINCT city) FROM station 
"""

"""
SELECT * FROM city WHERE countrycode = 'JPN';
"""

"""
(SELECT city, LENGTH(city)
FROM station 
WHERE LENGTH(city) = (SELECT MIN(LENGTH(city)) FROM station)
ORDER BY city 
LIMIT 1)
UNION ALL
(SELECT city, LENGTH(city)
FROM station 
WHERE LENGTH(city) = (SELECT MAX(LENGTH(city)) FROM station)
ORDER BY city 
LIMIT 1)
;
"""

# better (use with which acts like a precalculation?)
# WITH is a "Common Table Expression" (CTE)
"""
WITH cityLength AS (SELECT city, LENGTH(city) AS length FROM station)

(SELECT city, length
FROM cityLength
WHERE length = (SELECT MIN(length) FROM cityLength)
ORDER BY city
LIMIT 1)

UNION ALL -- This combines not just unique, but both all values from both selects

(SELECT city, length
FROM cityLength
WHERE length = (SELECT MAX(length) FROM cityLength)
ORDER BY city
LIMIT 1)
;
"""

"""
SELECT DISTINCT city 
FROM station
WHERE city LIKE 'a%' OR 
city LIKE 'e%' OR
city LIKE 'i%' OR
city LIKE 'o%' OR
city LIKE 'u%';
"""

# better
"""
SELECT DISTINCT city 
FROM station
WHERE LEFT(city, 1) IN ('a', 'e', 'i', 'o', 'u')
;
"""

"""
SELECT DISTINCT city
FROM station
WHERE RIGHT(city, 1) in ("a", "e", "i", "o", "u");
"""

"""
SELECT DISTINCT city
FROM station
WHERE LEFT(city, 1) IN ('a', 'e', 'i', 'o', 'u') AND
RIGHT(city, 1) IN ('a', 'e', 'i', 'o', 'u');
"""

"""
SELECT DISTINCT city 
FROM station 
WHERE LEFT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
;
"""

"""
SELECT DISTINCT city
FROM station
WHERE RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');
"""

"""
SELECT DISTINCT city
FROM station
WHERE LEFT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u') AND
RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');
"""

"""
SELECT name 
FROM students
WHERE marks > 75
ORDER BY RIGHT(name, 3), id;
"""

"""
SELECT name
FROM Employee
ORDER BY name;
"""

"""
SELECT name 
FROM Employee
WHERE salary > 2000 AND
months < 10
ORDER BY employee_id;
"""

"""
SELECT
    CASE
        WHEN (a + b <= c) OR (b + c <= a) OR (a + c <= b) THEN "Not A Triangle"
        WHEN (a = b AND b = c) THEN "Equilateral"
        WHEN (a = b OR b = c OR a = c) THEN "Isosceles"
        ELSE "Scalene"
    END
FROM triangles;
"""

#alternative; notice IF doesn't use THEN but CASE does. SQL is IF(condition, value_if_true, value_if_false)
"""
SELECT
    IF ((a + b <= c) OR (b + c <= a) OR (a + c <= b), "Not A Triangle",
    IF (a = b AND b = c, "Equilateral",
    IF (a = b OR b = c OR a = c, "Isosceles", "Scalene")))
FROM triangles;
"""

"""
(SELECT CONCAT(name, '(', LEFT(Occupation, 1), ')')
FROM Occupations
ORDER BY name)

UNION ALL

(SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.')
FROM Occupations
GROUP BY Occupation
ORDER BY COUNT(Occupation) ASC, Occupation)
"""

# Union and Union All seem to not preserve ordering, so global ordering still needed?
"""
SELECT *
FROM (
    (SELECT CONCAT(name, '(', LEFT(Occupation, 1), ')') AS result
    FROM Occupations
    ORDER BY Name)
    
    UNION ALL
    
    (SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.') AS result
    FROM Occupations
    GROUP BY Occupation
    ORDER BY Name)
) AS combined_results
ORDER BY
    CASE
        WHEN result LIKE 'There are%' THEN 1
        ELSE 0
    END,
    result;
"""

"""
SELECT COUNT(name)
FROM city
WHERE Population > 100000;
"""

"""
SELECT SUM(Population)
FROM city
WHERE District = 'California';
"""

"""
SELECT AVG(Population) 
FROM City
WHERE District = 'California';
"""

"""
SELECT ROUND(AVG(Population))
FROM City
"""

"""
SELECT SUM(Population)
FROM City
WHERE countryCode = 'JPN';
"""

"""
SELECT MAX(Population) - MIN(Population)
FROM City
"""

# Round up (CEILing) after computing difference of someone with a broken '0' key that
# Notice REPLACE works on Integer without converting to and fron TEXT/string
"""
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM Employees
"""

# notice that each column has an aggregating value (i.e. MAX() and COUNT()) (or doesn't in other cases)
# I think the max will only be calculated onece and then used to filter, not for each row
"""
SELECT MAX(Months * Salary), COUNT(*)
FROM Employee
WHERE Months * Salary = (SELECT MAX(Months * Salary) FROM Employee)
;
"""

"""
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)
FROM Station;
"""

"""
SELECT ROUND(SUM(LAT_N), 4)
FROM Station
WHERE 38.7880 < LAT_N AND
LAT_N < 137.2345;
"""

#why is this different than above?
"""
SELECT ROUND(SUM(LAT_N), 4)
FROM Station
WHERE 38.7880 < LAT_N < 137.2345;
"""

"""
SELECT ROUND(MAX(Lat_n),4)
FROM Station
WHERE Lat_n < 137.2345;
"""

"""
SELECT ROUND(Long_w, 4)
FROM Station
WHERE Lat_n < 137.2345
ORDER BY Lat_n DESC
LIMIT 1;
"""

"""
SELECT ROUND(Lat_n, 4)
FROM Station
WHERE Lat_n > 38.7780
ORDER BY Lat_n
LIMIT 1;
"""

"""
SELECT ROUND(Long_w, 4)
FROM Station
WHERE Lat_n > 38.7780
ORDER BY Lat_n
LIMIT 1;
"""

"""
SELECT SUM(City.Population)
FROM City
JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Continent = 'Asia';
"""

# is left join a little safer? we won't drop anything, but rather might get Nulls
"""
SELECT SUM(City.Population)
FROM City
LEFT JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Continent = 'Asia';
"""

"""
SELECT CITY.Name
FROM CITY
LEFT JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.Continent = 'Africa';
"""

"""
SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population))
FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;
"""

# this syntax works on ms sql server, but not mysql
"""
DECLARE @Counter INT
SET @Counter = 0

WHILE (@Counter < 20)
BEGIN
    PRINT REPLICATE('*', 20 - @Counter)
    SET @Counter = @Counter + 1
END
;
"""

# mysql version for a triangle of *
# notice the SET variable syntax and how it needs @ and a ; at the end
# the := sort of acts like the walrus operator := in Pyton (set and use all at once)
# using information.tables is a hack. we need a dummy table of at least 20 rows
"""
SET @counter := 21;

SELECT REPEAT('* ', @counter := @counter - 1) 
FROM information_schema.tables
WHERE @counter > 0
;
"""

"""
SET @counter := 0;

SELECT REPEAT("* ", @counter := @counter + 1)
FROM Information_Schema.tables
WHERE @counter < 20;
"""

"""
SELECT DISTINCT City
FROM STATION
WHERE LEFT(City, 1) NOT IN ('a', 'e', 'i', 'o', 'u') OR
RIGHT(City, 1) NOT IN ('a', 'e', 'i', 'o', 'u');
"""

#Manhattan Distance
"""
SELECT ROUND(MAX(LAT_N) - MIN(Lat_n) + MAX(Long_w) - MIN(Long_w), 4)
FROM STATION;
"""

#Euclidean distance
"""
SELECT ROUND(SQRT(POWER(MAX(LAT_N) - MIN(Lat_n), 2) + POWER(MAX(Long_w) - MIN(Long_w), 2)), 4)
FROM STATION;
"""

# assumes odd count with one number being the median
# who knew median was so tedious in sql?
# use where the @counter variable is after being incremented in the inner subquery
"""
-- assumes the list is odd length
SET @counter = 0;

SELECT ROUND(subquery.Lat_n, 4)
FROM
    (SELECT @counter := @counter + 1 AS idx, Lat_n
     FROM STATION
     ORDER BY Lat_n) AS subquery
WHERE subquery.idx = CEIL(@counter/2)
;
"""

# handles odd or even length lists
"""
SET @counter = -1;

SELECT ROUND(AVG(subquery.Lat_n), 4)
FROM
    (SELECT @counter := @counter + 1 AS idx, Lat_n
     FROM STATION
     ORDER BY Lat_n) AS subquery
WHERE subquery.idx IN (CEIL(@counter/2), FLOOR(@counter/2))
;
"""

# note: GROUP BY and ORDER BY should be consistent in some ways
"""
SELECT h.hacker_id, h.name
FROM HACKERS AS h
JOIN SUBMISSIONS AS s ON h.Hacker_id = s.Hacker_id
JOIN CHALLENGES c ON s.Challenge_id = c.Challenge_id
JOIN DIFFICULTY d ON c.difficulty_level = d.difficulty_level
WHERE s.score = d.score -- filters during query
GROUP BY h.hacker_id, h.name
HAVING COUNT(h.Hacker_id) > 1 -- filters after GROUP BY query
ORDER BY COUNT(h.Hacker_id) DESC, h.Hacker_id
;
"""

# note: this returns many lines/hacker_id even though original table has just one instance per hacker id
"""
SELECT h.hacker_id, h.name
FROM HACKERS AS h
JOIN SUBMISSIONS AS s ON h.Hacker_id = s.Hacker_id
JOIN CHALLENGES c ON s.Challenge_id = c.Challenge_id
JOIN DIFFICULTY d ON c.difficulty_level = d.difficulty_level
WHERE s.score = d.score -- filters during query
ORDER BY h.hacker_id;
"""

# notice the WHERE clause in the subquery using values in the outer query
"""
SELECT w.id, p.age, w.coins_needed, w.power
FROM WANDS AS w
JOIN WANDS_PROPERTY AS p ON w.code = p.code
WHERE w.coins_needed = (SELECT min(coins_needed)
    FROM WANDS AS ww 
    JOIN WANDS_PROPERTY AS pp ON ww.code = pp.code 
    WHERE pp.is_evil = 0 AND p.age = pp.age and w.power = ww.power)
ORDER BY w.power DESC, p.age DESC;
"""

"""
SELECT (CASE
            WHEN g.Grade >= 8 THEN Name ELSE NULL
        END), 
        g.Grade, 
        s.Marks
FROM STUDENTS AS s
JOIN GRADES g ON s.MARKS >= g.Min_mark AND s.MARKS <= g.Max_mark
ORDER BY g.Grade DESC, s.Name
;
"""

"""
SELECT h.hacker_id, h.name, COUNT(c.challenge_id)
FROM HACKERS AS h
JOIN Challenges AS c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name;
"""

"""
-- common table expression (first one gets challenge counts for each id)
WITH cte AS (SELECT h.hacker_id AS id, COUNT(c.challenge_id) AS counts
        FROM HACKERS AS h
        JOIN Challenges AS c ON h.hacker_id = c.hacker_id
        GROUP BY h.hacker_id),

-- second one is ued for WHERE filtering in main query. COUNT(COUNT()) to find ties (less than the max) (these can't be included)
cte2 AS (
    SELECT counts AS counts2, COUNT(*)
    FROM cte
    WHERE  counts < (SELECT MAX(counts) FROM cte) -- each line is filtered
    GROUP BY counts
    HAVING COUNT(*) > 1 -- final result is filtered, so aggregation condition OK
)

-- main query gets info from original cte and hackers table (and uses cte2 and WHERE - NOT IN to filter)
SELECT hacker_id, name, cte.counts
FROM Hackers h
JOIN cte ON h.hacker_id = cte.id
WHERE cte.counts NOT IN (SELECT counts2 FROM cte2)
ORDER BY cte.counts DESC, h.hacker_id
;
"""

"""

"""

result = session.execute(text(sql_query))
print(result, type(result))

session.close()