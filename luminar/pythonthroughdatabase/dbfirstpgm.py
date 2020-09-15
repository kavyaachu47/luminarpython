#import sqlconnector

import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin='mysql_native_password'
)

cursor=db.cursor()

#execute sql query

sql="SELECT VERSION()"
cursor.execute(sql)

#fetch a single row using fetchone() method

data=cursor.fetchone()
print("Database version:",data)

#disconnect from server

db.close()
