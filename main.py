import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')
#step 1
#display product deatils along with order details
# #productCode is the common column in both tables so we use it as the common key
# result = pd.read_sql("""
#                      SELECT * FROM orderdetails JOIN products
#                      ON orderdetails.productCode = products.productCode
#                      LIMIT 10;
#                      """, conn)
# print(result)

#step 2 USING clause instead of repeating the column names that are identical in both tables
# all_records = pd.read_sql("""
#                           SElECT * FROM orderdetails 
#                           JOIN products
#                           USING(productCode)
#                           LIMIT 10;
#                           """, conn)
# print(all_records)

#step 3 aliasing a table name to shorten the name or the overall query
#example using step 1
# results = pd.read_sql("""
#                       SELECT * FROM orderdetails AS od JOIN products as p
#                       ON od.productCode = p.productCode
#                       LIMIT 10;
#                       """)
# print(results)

#step 4 use LEFT JOIN to return all rows from the left table(orderdetails) 
# and the matched rows from the right table(products)
#if there is no match, the result is NULL on the right side of the table
query = pd.read_sql("""
                    SELECT * FROM products LEFT JOIN orderdetails
                    USING(productCode);
                    """ , conn)
print("Number of records returned:", len(query))
print("Number of records where order details are null:", len(query[query.orderNumber.isnull()]))
print(query[query.orderNumber.isnull()])

conn.close()