import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "rent_user",
    passwd = "livein_password",
    database = "rent_data"
)
sql = conn.cursor()