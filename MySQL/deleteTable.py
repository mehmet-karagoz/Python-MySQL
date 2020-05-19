import mysql.connector

mydb = mysql.connector.connect(
    host='yourhost(localhost)',
    user='youruser',
    passwd='yourPassword',
    database='databasename(mydatabase)'
)                               

mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address= 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")


# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")


# sql = "DROP TABLE customers"

# mycursor.execute(sql)


# sql = "DROP TABLE IF EXISTS customers"

# mycursor.execute(sql)