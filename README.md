This is a Structured Query Language (SQL) repository.

XAMPP was used to serve a MySQL database locally. (http://localhost/phpmyadmin/)

MySQL is a popular Relational DataBase Management System (RDBMS). It is usually considered the best place to start before using other RDBMS such as MS SQL Server, PostgreSQL, etc.

Here's a CREATE TABLE and INSERT INTO SQL statement. (You should also look at the CRUD file):

![XAMPP create table](/img/create_table_XAMPP.png)

We use python to query and keep the sqlalchemy query in text form as opposed to using methods like .WHERE(), .GROUPBY(), etc. See run_query.py and additional_SQL_queries.py

But developing in a .sql file can still be nice for autocomplete, linting, etc. 

