import pymysql as mysql

dataBase=mysql.connect(
    host="localhost",
    user="root",
    passwd="caddcenter"
)

cursorObject=dataBase.cursor()
#cursorObject.execute("create database company")
connect=mysql.connect(host="localhost",user="root",password="caddcenter",database="students")
curser=connect.cursor()
#curser.execute("create table employee(sname varchar(100),age int,id int,address varchar(300))")
#curser.execute("insert into employee(sname,age,id,address)values('ram','45','5678','cdmmmm'),('raj','65','3456','myllll'),('sam','23','55668','hummmm')")
curser.execute("select * from employee")
#details=curser.fetchall()
#print(details)
columns=[col[0] for col in curser.description]
print(columns)
"""curser.execute ("insert into employee(sname,age,id,address)values('banu','26','3400','3')")
curser.execute("update employee set id=29500 where sname='harish'")
curser.execute("select*from employee where sname like 'a%'")
a=curser.fetchall()
curser.execute("select * from employee where sname like 'b%'")
b=curser.fetchall()
print(a,b,sep="\n")"""
name="arun"
email="67"
phone="ruteeeee"
id="5678876"
curser.execute("insert into employee(sname,age,address,id)values(%s,%s,%s,%s)",(name,email,phone,id)) 
connect.commit()
print("data inserted succesfully")