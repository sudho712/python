import pymysql as db


conn=db.connect(host="localhost",user="root",password="",database="bank_db",port=3306)
curr=conn.cursor()
name=input('enter name')
email=input('enter email')
phone=input('enter phone')
balance=input('en1ter balance')
qry=f"insert into accounts(name,email,phone,balance) values('{name}','{email}','{phone}',{balance})"
curr.execute(qry)
conn.commit()
conn.close()