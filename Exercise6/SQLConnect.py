'''
Created on 19 Dec 2018

@author: QA
'''
#DRIVER
import pyodbc

print('Connectiong...')

connString = r'DRIVER={ODBC Driver 13 for SQL Server};'r'SERVER=.\SQLExpress;'r'DATABASE=TrafficData;'r'Trusted_Connection=yes'

print (connString)

conn = pyodbc.connect( connString )

print ('Connected')
cur = conn.cursor()
print ('Cursor Established')

sqlquery = "select * from Vehicle_Type"

resultSet = cur.execute(sqlquery).fetchall()

for row in resultSet :
    print ( row )
print ("{} rows returned ".format(len(resultSet)))

conn.close()
print ('Connection Closed')
