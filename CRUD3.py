import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="17april")
cur = con.cursor()
# sql = "create database 17april"
# sql = "create table emp(emp_id int(3) primary key,first_name varchar(20),last_name varchar(20),email_id varchar(20),address varchar(20))"
# sql = "insert into emp values(103, 'Mohan' , 'Ahuja' , 'Mohan@892' , 'Hyderabad')"
# sql = "alter table emp add hobbies varchar(20)"
# sql = "alter table emp drop column hobbies"
# sql = "delete from emp where emp_id=103"
# sql = "update emp set first_name='Rohit' where address='Indore'"
sql = "select * from emp"
try:
    cur.execute(sql)
except Exception as e:
    print(e)
    con.rollback()
else:
    # print("Database created")
    # print("Table Created")
    # print("Data Inserted")
    # print("Table Altered")
    # print("record deleted")
    # print("record updated")
    # con.commit()
    result = cur.fetchall()
    for r in result:
        print(r)
finally:
    con.close()