# Connects to the database on the other Raspberry PI
mydb = mysql.connector.connect(
  host="192.168.50.100",
  user="root",
  passwd="root",
  database="LampAppProfiles")