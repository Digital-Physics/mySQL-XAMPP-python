-- https://www.youtube.com/watch?v=HXV3zeQKqGY

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

CREATE TABLE branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL -- When REFERENCES get DELETEd, SET FOREIGN KEY value to NULL
);

-- now we can add a foreign key to the first table
ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

-- note that it can have a foreign id in the same table (self-refrencing)
ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id) -- supervisor is also an employee in the same table
ON DELETE SET NULL;

CREATE TABLE client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(40),
    branch_id INT,
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL 
);

-- Composite PRIMARY KEY that is also the FOREIGN KEY
CREATE TABLE works_with (
    emp_id INT,
    client_id INT,
    total_sales INT,
    PRIMARY KEY(emp_id, client_id)
    FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE -- When REFERENCES get DELETEd, delete FOREIGN KEY record
    FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);

CREATE TABLE branch_supplier (
    branch_id INT,
    supplier_name VARCHAR(40),
    supply_type VARCHAR(40),
    PRIMARY KEY(branch_id, supplier_name),
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

-- now it's time to INSERT INTO table VALUES, let's start with the Corporate branch...

-- Notice we need NULL on FOREIGN KEY since it isn't available yet, just like we had to ALTER TABLE
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

-- complete this process later
-- https://youtu.be/HXV3zeQKqGY?si=6S3UdPmdmPxbyP5A&t=8045