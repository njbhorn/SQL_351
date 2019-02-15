'''
Created on 19 Dec 2018

@author: QA
'''
#DRIVER
import pyodbc

def displayException ( exception ):
    info = exception.args[1]
#     print("raw : " + info)
    info = info.replace('[','')
#     print("repl [ : " + info)
    info = info.replace(']',',')
#     print("repl ] : " + info)
    info = info.split(',')
#     print ( "ERROR = " + info [ len(info) - 1])
    return info [ len ( info ) - 1  ]
#     print(info[ (len(info) - 1) : len(info)])

print('Connectiong...')

try :

    connString = r'DRIVER={ODBC Driver 13 for SQL Server};'r'SERVER=.\SQLExpress;'r'DATABASE=TrafficData;'r'Trusted_Connection=yes'
    
    print (connString)
    
    conn = pyodbc.connect( connString )
    
    print ('Connected')
    cur = conn.cursor()
    print ('Cursor Established')
    
    sqlquery = "select code, description  from Vehicle_Type"
    
    resultSet = cur.execute(sqlquery).fetchall()
    
    for row in resultSet :
        print ( row )
    print ("{} rows returned ".format(len(resultSet)))
    
    conn.close()
except Exception as ex:
    print(displayException(ex))
#     if ex.args[0] == '08001':
#         print("Cannot connect to Server")
#     elif ex.args[0] == '28000':
#         print("Login failed - check connection string")
#     for arg in ex.args:
#         print(arg + '\n')
    
print ('Connection Closed')
