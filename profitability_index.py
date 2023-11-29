import sqlite3
import pandas as pd
import support

# Connect to the SQLite database
conn = sqlite3.connect(support.path_database)  # Replace your_database_name.db' with the actual name of your SQLite database file

# Define your SQL query to join the tables
query = '''
    SELECT p.model, p.type, l.speed, l.ram, l.hd, l.price 
    FROM laptop l
    JOIN product p ON l.model = p.model
    WHERE p.type = 'laptop'
    UNION
    SELECT p.model, p.type, pc.speed, pc.ram, pc.hd, pc.price
    FROM pc
    JOIN product p ON pc.model = p.model
    WHERE p.type = 'pc';
'''

# Use pandas to read the query result into a DataFrame
df = pd.read_sql_query(query, conn)

# Calculate the profitability index
df['profitability_index'] = ((df['ram'] + df['hd']) / df['price']) * df['speed']

# Print the resulting DataFrame
print(df[['model', 'type', 'profitability_index']])

# Close the database connection
conn.close()
