import mysql.connector
mydb = mysql.connector.connect(
    host = "10.200.14.24",
    port = 3306,
    user = "edmalema",
    password = "norge123"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE musikk CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
print(mycursor.rowcount, "record(s) affected")