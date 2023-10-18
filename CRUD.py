#CRUD: Create, read, update, delete.
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="12april") #to create connection between mysql and python
cur = con.cursor()      #to execute query in mysql we create cursor with the connection object(con)
# sql = "create database 12april"              #we create a database and store it in a variable
# sql = "create table emp(empid int(3) primary key,empname Varchar(30))"
# sql = "alter table emp add cityname varchar(20)"
# sql = "drop table emp"
# sql = "drop database 12april"
sql = "insert into emp values(101,'Shivam','Pune')"
try:
    cur.execute(sql)                 #execute the query in the try block with the help of cursor
except Exception as e:
    print(e)
    con.rollback()             #if any exception occurs then rollback() happens
else:
    # print("Database created")
    # print("Table created")
    # print("Table altered")
    # print("Table dropped")
    # print("Database dropped")
    con.commit()               #if exception does not occurs then the changes will save permanently
finally:
    con.close()               #at last close the connection

