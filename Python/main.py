import sqlite3
import support

connection = sqlite3.connect('C:\\Users\\filip\\OneDrive\\Pulpit\\inpost zadanie\\DB_computers.db')

cursor = connection.cursor()

command1 = """SELECT * FROM laptop"""

cursor.execute(command1)

results = cursor.fetchall()
print(results)



