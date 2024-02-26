"""A.C.I.D. for Transactions (a single unit of work) of databases are principles for data integrity"""
# we wouldn't want to deduct $50 from one account without putting it into someone eles'e account balance

"""
Atomicity: In SQL, atomicity is typically achieved through the use of transactions. A transaction 
is a sequence of one or more SQL operations (e.g., INSERT, UPDATE, DELETE) that are treated as a 
single unit. If any part of a transaction fails (e.g., due to a constraint violation or an error), 
the entire transaction is rolled back, and the database is left unchanged.

Consistency: SQL databases use constraints, such as primary keys, foreign keys, and check constraints, 
to enforce data consistency. These constraints ensure that data remains valid and consistent throughout the database.

Isolation: Isolation in SQL databases refers to the ability to run multiple transactions concurrently without 
affecting each other. SQL databases use locking mechanisms to achieve isolation. For example, when one transaction 
is updating a row, other transactions are prevented from modifying that same row until the first transaction completes.

Durability: Durability in SQL databases ensures that once a transaction is committed, its changes are permanent and will 
not be lost, even in the event of a system failure. SQL databases achieve durability by writing transaction logs to disk, 
which can be used to recover the database in the event of a failure.
"""

"""
-- Create a table for bank accounts
CREATE TABLE bank_accounts (
    account_id INT PRIMARY KEY,
    balance DECIMAL(10, 2)
);

-- Insert some sample data
INSERT INTO bank_accounts (account_id, balance) VALUES (1, 1000.00);
INSERT INTO bank_accounts (account_id, balance) VALUES (2, 500.00);

-- Start a transaction
BEGIN TRANSACTION;

-- Transfer money from account 1 to account 2
UPDATE bank_accounts SET balance = balance - 100.00 WHERE account_id = 1;
UPDATE bank_accounts SET balance = balance + 100.00 WHERE account_id = 2;

-- Simulate a failure (e.g., power outage) before committing
-- ROLLBACK;

-- Commit the transaction
COMMIT;

-- Display the updated balances
SELECT * FROM bank_accounts;
"""

"""
In this example, we begin a transaction using BEGIN TRANSACTION, then perform two UPDATE statements 
to transfer money between two bank accounts. If a failure were to occur (e.g., a power outage) before 
we commit the transaction, we can use ROLLBACK to undo the changes. However, if the transaction 
completes successfully, we use COMMIT to make the changes permanent.

This demonstrates the atomicity of the transaction, as either both UPDATE statements succeed (and the 
transfer is completed) or they both fail (and the transfer is rolled back). It also illustrates the durability 
property, as once the transaction is committed, the changes are permanent and survive a system failure.
"""