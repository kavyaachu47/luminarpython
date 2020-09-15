import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="luminar",
    auth_plugin="mysql_native_password"
)
print(db)
cursor=db.cursor()
sql="INSERT INTO EMPLOYEE(EIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('ANU','SAM',23,'F',30000)"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()
