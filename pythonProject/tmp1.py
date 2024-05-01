import pyodbc
from datetime import datetime

connectionString = (r'Driver={SQL Server};Server=DESKTOP-KB73HD6;Database=aurora1;Trusted_Connection=yes;')
connection = pyodbc.connect(connectionString)
dbCursor = connection.cursor()

requestString = """select id, title from sphere"""
dbCursor.execute(requestString)
for row in dbCursor:
	print(row.id, row.title)
