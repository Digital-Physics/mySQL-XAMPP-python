"""
Defining primary and foreign keys in your table is not necesary, but can prevent several types of errors related to data integrity and consistency:

Insertion Errors: Primary keys ensure that each row in a table is uniquely identified. If you try to insert a row with a primary key that already exists in the table, the database will raise an error, preventing duplicate entries.

Update Errors: Foreign keys enforce referential integrity between tables. If you try to update a foreign key value to a value that does not exist in the referenced table's primary key column, the database will raise an error, preventing orphaned or inconsistent data.

Deletion Errors: Similarly, foreign keys can prevent deletion of a record in the primary key table if there are related records in the foreign key table. This helps maintain data integrity by preventing accidental deletion of important data.

Data Consistency: By enforcing relationships between tables, primary and foreign keys help ensure that data remains consistent across tables. For example, if you have a foreign key constraint between an "orders" table and a "customers" table, you can ensure that each order is associated with a valid customer.

Overall, defining primary and foreign keys helps maintain the integrity and consistency of your database, reducing the risk of data errors and inconsistencies.
"""


# https://www.youtube.com/watch?v=HXV3zeQKqGY&t=7154s 
# Note: the first CREATE TABLE in a Database can't have FOREIGN keys defined right away.
"""
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    birth_day DATE,
    sex VARCHAR(1),
    salary INT,
    super_id INT
    branch_id INT
);
"""

"""
CREATE TABLE branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);
"""

# now we can add a foreign key to the first table
"""
ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;
"""

# note that it can have a foreign id in the same table (self-refrencing)
"""
ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id) -- supervisor is also an employee in the same table
ON DELETE SET NULL;
"""

"""
...
"""