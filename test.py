import mysql.connector

print(dir(mysql))

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root"
# )

# print(mydb)

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE wk6")
# mycursor.execute("USE wk6")
# mycursor.execute("CREATE table user (account INTEGER PRIMARY KEY, password varchar(255), name varchar(255))")


# mycursor.execute("SELECT * FROM user")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
   print(x)
  