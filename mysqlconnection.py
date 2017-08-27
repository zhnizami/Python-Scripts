import mysql.connector
try:
    sqlconnection = mysql.connector.connect(user='root',password='1234',host='localhost')
    sqlcursor = sqlconnection.cursor()
except:
    print("Connection Failed!")
else:
    print("Connection Successful!")
    print("Connection Name: 'sqlconnection'")
    print("Cursor Name:'sqlcursor'")
  
