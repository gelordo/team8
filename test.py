import mysql.connector

conn = mysql.connector.connect(
    host="sql11.freesqldatabase.com",
    user="sql11672526",
    password="QVkl1fXMYs",
    database="sql11672526"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Profesori")
cursor.execute("SELECT * FROM ")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close() 
