from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

engine = create_engine(f"mysql+pymysql://{env_vars['APP_USER']}:{env_vars['PASSWORD']}@{env_vars['HOST']}:{env_vars['DB_PORT']}/{env_vars['DATABASE']}")

Session = sessionmaker(bind=engine)
session = Session()

sql_query = """
SELECT 
    AVG(daily_sums.total_amount) AS three_day_average
FROM
  (SELECT 
      DATE(transaction_time) AS transaction_date,
      SUM(transaction_amount) AS total_amount
    FROM transactions 
    WHERE transaction_time BETWEEN '2021-01-29 00:00:00' AND '2021-01-31 23:59:59'
    GROUP BY DATE(transaction_time)
  ) AS daily_sums;
"""

result = session.execute(text(sql_query))
print(result, type(result))

three_day_average = result.scalar()
print(f"January 31's rolling 3 day average of total transaction amount processed per day: {three_day_average:.2f}")

session.close()