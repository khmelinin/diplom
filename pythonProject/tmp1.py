import pyodbc
from datetime import datetime

connectionString = (r'')
connection = pyodbc.connect(connectionString)
dbCursor = connection.cursor()

requestString = """select id, title from sphere"""
dbCursor.execute(requestString)
for row in dbCursor:
	print(row.id, row.title)
