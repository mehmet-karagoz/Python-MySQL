import mysql.connector

mydb = mysql.connector.connect(
    host='yourhost(localhost)',
    user='youruser',
    passwd='yourPassword',
    database='databasename(mydatabase)'
)                               

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")  #tablodaki herseyi secer

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)


# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")  #2. siradan baslar

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)



# mycursor.execute("SELECT name, address FROM customers")  #tablodaki istenen seyleri getirir

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()  #tekli secim yapar

# print(myresult)


# sql = "SELECT * FROM customers WHERE address='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(myresult)

# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(myresult)

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers ORDER BY name DESC"  #tersten siralar

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)