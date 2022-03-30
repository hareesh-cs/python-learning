import mysql.connector as conn

mydb = conn.connect(host='localhost', user='root', passwd="root")
cursor = mydb.cursor()

# cursor.execute("create database test_db")
cursor.execute("use test_db")
# cursor.execute('create table student_table(student_id INT(10) ,firstname VARCHAR(30)  ,lastname VARCHAR(30) ,reg_id INT(10) ,class_name VARCHAR(30))')
cursor.execute('show tables')
print(cursor.fetchall())
cursor.execute('insert into student_table values(423423 , "Hareesh" , "Sikakollu" , 2344323 , "Python")')
mydb.commit()
cursor.execute('select * from student_table')
print(cursor.fetchall())