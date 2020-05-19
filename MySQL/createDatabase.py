import mysql.connector

mydb = mysql.connector.connect(
    host='yourhost(localhost)',
    user='youruser',
    passwd='yourPassword',
    database='databasename(mydatabase)'
)                               

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")  #database olusturma

# mycursor.execute("SHOW DATABASES")  #database leri gosterir

# for x in mycursor:
#     print(x)