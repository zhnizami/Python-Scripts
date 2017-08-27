class MySqlClass:
    global conn
    global cursor
    def __init(self):
         print("")

         
    def createDatabase(self):
        try:
            cursor.execute("create database "+self.name)
        except:
            print("Cannot create database!")
        else:
            print("Successful!")

            
    def insertMethod(self):
        try:
            tbname=input("Table Name:")
            iden=input("Enter Id:")
            fname=input("Enter Full Name:")
            email= input("Enter Email:")
            phone= input("Enter Contact:")
            city=input("Enter City:")
            print("________________________________")
            we=input("Save Record? Y/N")
            if we=="Y":
                cursor.execute("use "+self.name)
                cursor.execute("INSERT INTO "+tbname+" VALUES('"+iden+"','"+fname+"','"+email+"','"+phone+"','"+city+"')")
                conn.commit()
                print("Record saved successfully!")
        except:
            print("Insertion Error!")

            
    def setname(self,name):
        self.name=name
        
    def createTable(self):        
        try:
            r= 1
            pfk= False
            while r==1:
                nnl="null"
                tbname=input("Table Name:")
                clname = input("Column Name:")
                cldt=input("Data Type:")
                if pfk==False:
                    g=input("Is this column a primary key? Y/N")
                    if g=="Y":
                        pfk=True
                        nnl="not null"
                    s= input("Save?Y/N")
                    if s=="Y" and pfk==True:
                        cursor.execute("create table"+tbname +"("+clname+" " +cldt+" primary key "+" "+ nnl+")")     
                r=int(input("Add another column? 1/0"))
        except:
            print("Error")
        else:
            print("")
            
    def  updateMethod(self):
        try:
            tbname=input("Table Name:")
            iden=input("Enter Id:")
            fname=input("Enter Full Name:")
            email= input("Enter Email:")
            phone= input("Enter Contact:")
            city=input("Enter City:")
            print("________________________________")
            we=input("Update Record? Y/N")
            if we=="Y":
                cursor.execute("use "+self.name)
                cursor.execute("UPDATE "+tbname+" SET Fullname='"+fname+"',email='"+email+"',phone='"+phone+"',city='"+city+"' where id='"+iden+"'")
                conn.commit()
                print("Record updated successfully!")
        except:
            print("Updation Error!")
            
    def  deleteMethod(self):
        try:
            tbname=input("Table Name:")
            iden=input("Enter Id:")
            cursor.execute("use "+self.name)
            cursor.execute("delete from "+tbname+ " where id='"+iden+"'")
            conn.commit()
            print("Record Deleted Succesfully!")
        except:
            print("Deletion Error!")
    def showMethod(self):
        try:
            cursor.execute("use "+self.name)
            tbname = input("Table Name:")
            cursor.execute("select * from "+tbname)
            print(cursor.fetchall())
        except:
            print("Can not show records!")
    def deleteDatabase(self):
        try:
            cursor.execute("drop database "+self.name)
            conn.commit();
            print("Database deleted Successfully!")
        except:
            print("Can not delete database!")
    def __del__(self):
        print("")

import mysqlconnection
mysqlclass = MySqlClass()
try:
    conn= mysqlconnection.sqlconnection
    cursor= mysqlconnection.sqlcursor
except:
    print("Connection Error!")
else:
    print("Connection Succesfull!")
rep=1
while rep==1:
    print("Please enter the database name:")
    dbname=input()
    mysqlclass.setname(dbname)
    print("___________________________________")
    print("Press 1 to create database")
    print("Press 2 to create table")
    print("Press 3 to insert a record")
    print("Press 4 to update a record")
    print("Press 5 to delete a record")
    print("Press 6 to delete a database")
    print("Press 7 to show all records")
    print("___________________________________")
    reply= int(input())
    print("___________________________________")
    if reply==1:
        mysqlclass .setname(dbname)
        mysqlclass.createDatabase()
    elif reply==2:
        mysqlclass.createTable
    elif reply==3:
        mysqlclass .setname(dbname)
        mysqlclass.insertMethod()
    elif reply==4:
        mysqlclass .setname(dbname)
        mysqlclass.updateMethod()
    elif reply==5:
        mysqlclass.setname(dbname)
        mysqlclass.deleteMethod()
    elif reply==6:
        mysqlclass.setname(dbname)
        mysqlclass.deleteDatabase()
    elif reply==7:
        mysqlclass.setname(dbname)
        mysqlclass.showMethod()
    rep=int(input("Do you want to perform another operation? 1/0"))








    


