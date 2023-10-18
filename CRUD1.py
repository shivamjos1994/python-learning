import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="root")
cur = con.cursor()
sql = "create database 13april"
try:
    cur.execute(sql)
except Exception as e:
    print(e)
    con.rollback()
else:
    print("Database created")
    con.commit()
finally:
    con.close()