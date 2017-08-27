print("Python with MySQL Server")
import mysql.connector
try:
    conn= mysql.connector.connect(user='root',password='1234',host='localhost',database='firstoracledatabase')
except:
    print("Connection Error!")
else:
    print("Connection Successfull!")

def mySqlQueries():
    try:
        cursor= conn.cursor()
        print("Write the query you want to execute")
        query = input()
        cursor.execute(query)
    except:
        print("Can not execute query!")
    else:
        print(cursor.fetchall())

mySqlQueries()
