# BETWEEN
"""
SELECT * FROM Orders
WHERE OrderDate BETWEEN '2024-01-01' AND '2024-01-31';
"""

# extract the MONTH()
"""
SELECT * FROM Orders
WHERE MONTH(OrderDate) = 1; -- This will select all orders from January
"""

# CURRENT_
"""
SELECT CURRENT_DATE AS CurrentDate, CURRENT_TIME AS CurrentTime, CURRENT_TIMESTAMP AS CurrentTimestamp;
"""

# DATE_ADD() INTERVAL
"""
SELECT OrderDate, DATE_ADD(OrderDate, INTERVAL 7 DAY) AS NewOrderDate
FROM Orders;
"""

# DATE_SUB( , INTERVAL )
"""
SELECT DATE_SUB('2024-02-26', INTERVAL 4 WEEK);
"""

# DATEDIFF(,)
"""
SELECT DATEDIFF('2024-02-20', '2024-02-15') AS DateDifference;
"""

# DATE_FORMAT()
"""
SELECT DATE_FORMAT(OrderDate, '%Y-%m-%d') AS FormattedDate
FROM Orders;
"""