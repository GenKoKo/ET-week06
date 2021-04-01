import mysql.connector

# print(dir(mysql))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE wk6")
mycursor.execute("USE wk6")
mycursor.execute("CREATE table users06 (username varchar(255) NOT NULL , password varchar(255) NOT NULL, name varchar(255) NOT NULL, PRIMARY KEY(username))")
mycursor.execute("INSERT INTO users (name, username, password) VALUES(%s, %s, %s)",('test1','test-1','test_1'))

mycursor.execute("SELECT * FROM users")
# mycursor.execute("SHOW DATABASES")
for x in mycursor:
   print(x)
  