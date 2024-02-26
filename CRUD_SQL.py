from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
engine = create_engine(f"mysql+pymysql://{env_vars['APP_USER']}:{env_vars['PASSWORD']}@{env_vars['HOST']}:{env_vars['DB_PORT']}/{env_vars['DATABASE']}")
Session = sessionmaker(bind=engine)
session = Session()

# CRUD = create, read, update, delete (four basic operations for database management)
# CREATE 
#   CREATE TABLE student (,,);
#   ALTER TABLE student ADD gpa DECIMAL(3,2);
# Read
#   SELECT * FROM student;
# UPDATE
#   UPDATE TABLE student SET name ='bob'; -- UPDATE changes a field
#   INSERT INTO student VALUES (), (); -- INSERT INTO adds VALUES or rows to the table
# DELETE 
#   DELETE FROM table WHERE name = 'bob'; -- 'delete specifict records'
#   DROP TABLE student; -- 'drop entire tables'
#   TRUNCATE TABLE student; -- 'truncate all records but keep the table'

# make a database via XAMPP rather than
"""create database new_database_with_some_tables"""

# some of the main data types
"""
INT  
DECIMAL(10,4) -- exact value decimal 10 total digits and 4 after the decimal 
FLOAT
VARCHAR(20) -- string of text length 20 
BLOB -- Binary Large Object (for like images or files stored)
DATE -- 'YYYY-MM-DD' 
TIMESTAMP -- 'YYYY-MM-DD HH:MM:SS' -- notice DATE and TIMESTAMP use order of significance 
"""

# all these fields have additional info after the basic field type definition
# AUTO_INCREMENT could be used for student_id if you didn't want to put numbers in explicitly in INSERT INTO students VALUES (), (), ();
sql_create = """
CREATE TABLE student (
    student_id INT PRIMARY KEY, -- PRIMARY KEY is implicitly NOT NULL and UNIQUE
    name VARCHAR(20) NOT NULL, -- need a name when INSERT INTO student VALUES (), (), ();
    major VARCHAR(15) DEFAULT 'undecided', -- could add UNIQUE afterwards if we wanted each row's major to be unique. #Montessori
);
"""

# 
sql_describe = "DESCRIBE student;"

# ALTER TABLE student ADD
sql_alter_table = "ALTER TABLE student ADD gpa DECIMAL(3,2)"
sql_alter_table = "ALTER TABLE student DROP gpa"

sql_read = """
SELECT * FROM student
WHERE name = 'Bob' AND major = 'Math' 
"""

sql_insert_into_values = """
INSERT INTO student 
VALUES
    (1, 'Jack', 'Biology'),
    (2, 'Kate', 'Math'),
;
"""

sql_insert_into_values = """
INSERT INTO student
    ('id', 'name')
VALUES
    (3, 'Claire'), -- will be NULL for Major field
;
"""

# UPDATE table SET column =
sql_set = """
UPDATE student
SET major = 'BIO'
WHERE major = 'BIOLOGY'
;"""

# DELETE FROM table WHERE 
# for deleting whole rows or tables
sql_delete_from = """
DELETE FROM student
WHERE student_id = 5"""

sql_drop_table = "DROP TABLE student"

result = session.execute(text(sql_read))
print(result, type(result))

session.close()