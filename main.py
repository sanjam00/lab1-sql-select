import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')
# cur = conn.pd

df_first_five = pd.read_sql("""
                            SELECT employeeNumber, lastName FROM employees;
                            """, conn)

df_five_reverse = pd.read_sql("""
                            SELECT lastName, employeeNumber FROM employees;
                            """, conn)

df_alias = pd.read_sql("""
                            SELECT lastName, employeeNumber AS ID FROM employees;
                            """, conn)

df_executive = pd.read_sql("""
                           SELECT
                           CASE
                           WHEN jobTitle = "President" THEN "Executive"
                           WHEN jobTitle = "VP Sales" THEN "Executive"
                           WHEN jobTitle = "VP Marketing" THEN "Executive"
                           ELSE "Not executive"
                           END AS role
                           FROM employees;
                           """, conn)

df_name_length = pd.read_sql("""
                             SELECT length(lastName) AS name_length
                             FROM employees;
                             """, conn)

df_short_title = pd.read_sql("""
                             SELECT substr(jobTitle, 1, 2) AS short_title
                             FROM employees;
                             """, conn)

sum_total_price = pd.read_sql("""
                              SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
                              FROM orderDetails;
                              """, conn).values[0]

print(sum_total_price)

df_day_month_year = pd.read_sql("""
                                SELECT orderDate,
                                substr(orderDate, 9, 10) AS day,
                                substr(orderDate, 6, 6) AS month,
                                substr(orderDate, 1, 4) AS year
                                FROM orders;
                                """, conn)

print(df_day_month_year)