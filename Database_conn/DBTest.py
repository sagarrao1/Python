import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",  passwd="admin", database="sys")
mycursor= mydb.cursor()

mycursor.execute("select * from sys.student")
for i in mycursor:
    print(i)