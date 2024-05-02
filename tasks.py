"""
    Работу выполнил Панфилов В.А.
    Зависимости:
        Интерпретатор >python 3.10
        pscopg2
        pyodbc
    Для проверки необходимо раскомментировать задачи 3,7,9,10 и добавить токен подключения(user,pass,dbname ...)
"""
#Задача 1
print("ЗДАЧА 1")

from math import prod

def F(A):
    res = prod(range(2,A))
    return res

print(F(5))
print()

#Задача 2
print("ЗДАЧА 2")

import random

def task2(a:int=5, b:int=6):
    A=sorted([ random.randint(1,100) for _ in range(a) ])
    B=sorted([ random.randint(1,100) for _ in range(b) ])
    print(f"{A=},{B=}")
    for i in range(a+b,0,-1):
        if i>b:
            print(f"A[{i-b-1}]=",A[i-b-1])
        else:
            print(f"B[{i-1}]", B[i-1])

task2()
print()

#Задача 3
print("ЗАДАЧА 3")

A=5
B=10
print(f"{A=},{B=}")
A,B = max(A,B),min(A,B)
print(f"{A=},{B=}")
print()

#Задача 4
print("ЗАДАЧА 4")

#import psycopg2

#conn = psycopg2.connect("")
#cur = conn.cursor()

request = "SELECT\
    Date,\
    Amount,\
    SUM(Amount) OVER (ORDER BY Date) AS RunningTotal\
FROM\
    TBL;"

#cur.execute(request)
print(f"{request=}")
print()

#Задача 5
print("ЗАДАЧА 5")

def task5(A):
    B = (A*-11)-1
    return B

print(task5(-1))
print()

#Задача 6
print("ЗАДАЧА 6")

def task6(arr:int = [0,1,2,3,5,6]):
    b = 0
    for i in arr:
        if i != b:
            return b
        b+=1

print(task6())
print()

#Задача 7
print("ЗАДАЧА 7")

#import psycopg2

#conn = psycopg2.connect("")
#cur = conn.cursor()

request = "WITH Recursion AS (\
  SELECT StockID, Quantity, 1 AS Number\
  FROM TBL\
  UNION ALL\
  SELECT StockID, Quantity, Number + 1\
  FROM Recursion\
  WHERE Number < Quantity\
)\
SELECT NUM.ID, Recursion.StockID\
FROM NUM\
CROSS JOIN Recursion\
ORDER BY Recursion.StockID, NUM.ID;"

#cur.execute(request)
print(f"{request=}")
print()

#Задача 8
print("ЗАДАЧА 8")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def F(n):
    result = 1
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i
        result *= factorial
    
    return result

print(F(4))
print()

#Задача 9
print("ЗАДАЧА 9")

#import pyodbc

#table_name = "@TableName"
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=SERVERNAME;'
#                      'Database=DATABASE;'
#                      'Trusted_Connection=yes;')


#cursor = conn.cursor()
query = "SELECT DISTINCT\
            OBJECT_SCHEMA_NAME(obj.object_id) AS SchemaName,\
            OBJECT_NAME(obj.object_id) AS ObjectName,\
            obj.type_desc\
        FROM\
            sys.sql_modules mod\
            INNER JOIN sys.objects obj ON mod.object_id = obj.object_id\
        WHERE\
            mod.definition LIKE '%' + ? + '%'\
            AND obj.type_desc = 'SQL_STORED_PROCEDURE';"
#cursor.execute(query, table_name)
#results = cursor.fetchall()
#cursor.close()
    
print(query)

#Задача 10
print("ЗАДАЧА 10")

#import psycopg2

#conn = psycopg2.connect("")
#conn.autocommit = True
#cursor = conn.cursor()

table_name = "TBL"
substring = "example"

# SQL-запрос
query = """
    WITH CTE AS (
        SELECT
            ID,
            String,
            LENGTH(String) - LENGTH(REPLACE(String, %s, '')) AS Occurrences
        FROM
            {0}
        WHERE
            String LIKE '%' || %s || '%'
    )
    SELECT
        ID,
        String,
        Occurrences AS Quantity,
        ROUND(Occurrences * 100.0 / SUM(Occurrences) OVER(), 2) AS Percent
    FROM
        CTE
    WHERE
        Occurrences > 0;
""".format(table_name)

#cursor.execute(query, (substring, substring))
#results = cursor.fetchall()
