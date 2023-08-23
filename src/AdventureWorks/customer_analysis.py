import pandas as pd
import sqlite3
import pyodbc

# Connect to local AdventureWorks2022 database
conn_str = (
    r'driver={SQL Server};'
    r'server=(local);'
    r'database=AdventureWorks2022;'
    r'trusted_connection=yes;'
    )

cnxn = pyodbc.connect(conn_str)

cursor = cnxn.cursor()

# Verify proper connection to local database
query = "SELECT * FROM SYSOBJECTS WHERE xtype = 'U';"

df_existing_tables = pd.read_sql(query, cnxn)
print(df_existing_tables)

# Count total number of columns
query = "SELECT COUNT(NAME) AS [Total Number of Tables] FROM SYSOBJECTS WHERE xtype = 'U';"

df_existing_tables = pd.read_sql(query, cnxn)
print(df_existing_tables)


# Create new database
#cursor.execute(f"CREATE DATABASE {db_name}")

"""
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

"""

query = "EXEC sp_columns 'SalesReason';"

df_existing_columns = pd.read_sql(query, cnxn)
print(df_existing_columns)
stop
query = '''
        SELECT * 
            FROM AdventureWorks2022
        ;
            '''

df_Customer = pd.read_sql(query, cnxn)
print(df_Customer)

stop
# Verify proper connection to local database
query = "SELECT NAME FROM SYSOBJECTS WHERE xtype = 'U';"

df_existing_tables = pd.read_sql(query, cnxn)
print(df_existing_tables)

# Verify proper connection to local database
query = "SELECT ROUND(SUM(SalesOrderDetail.UnitPrice), 2) AS [Total Sales] FROM SYSOBJECTS;"

df_existing_tables = pd.read_sql(query, cnxn)
print(df_existing_tables)