# Imports
import mysql.connector

# Connects to the database on the other Raspberry PI
mydb = mysql.connector.connect(
  host="192.168.50.100",
  user="root",
  passwd="root",
  database="lampapplication")

# Fetch dB values from the Mysql database
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM profiles where name = 'current'")
data = mycursor.fetchall()
for row in data:
  profilename = str(row[1])
  dbmin = int(row[2])
  dbmax = int(row[3])