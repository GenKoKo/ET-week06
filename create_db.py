import mysql.connector

# print(dir(mysql))

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd=""
)

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE wk6")
mycursor.execute("USE wk6")
mycursor.execute("CREATE table user (username varchar(20) NOT NULL , password varchar(20) NOT NULL, name varchar(255) NOT NULL, PRIMARY KEY(username))")
mycursor.execute("INSERT INTO user (name, username, password) VALUES(%s, %s, %s)",('test_name','test_username','test_password'))
mydb.commit()

print(mycursor.rowcount, "inserted")

  
