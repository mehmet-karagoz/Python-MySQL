import mysql.connector

mydb = mysql.connector.connect(
    host='yourhost(localhost)',
    user='youruser',
    passwd='yourPassword'
)

print(mydb)