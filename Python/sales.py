import sqlite3
import pandas as pd
import support

# Connect to the SQLite database
conn = sqlite3.connect(support.path_database)  # Replace your_database_name.db' with the actual name of your SQLite database file

# Define your SQL query to join the tables
query = '''
    SELECT p.model, l.price, p.type
    FROM laptop l
    JOIN product p ON l.model = p.model 
    WHERE p.type = 'laptop'
    UNION
    SELECT p.model, pc.price, p.type
    FROM pc
    JOIN product p ON pc.model = p.model
    WHERE p.type = 'pc'
    UNION
    SELECT p.model, pr.price, p.type
    FROM printer pr
    JOIN product p ON pr.model = p.model
    WHERE p.type = 'printer'

'''

# Use pandas to read the query result into a DataFrame
df = pd.read_sql_query(query, conn)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
print(df)
# Calculate the profitability index
# df["sales"]=
# df = pd.DataFrame(data)

# Randomly select a PC, printer, and laptop
random_pc = df[df['type'] == 'pc'].sample(n=1)
random_printer = df[df['type'] == 'printer'].sample(n=1)
random_printer_2 = df[df['type'] == 'printer'].sample(n=1)
random_laptop = df[df['type'] == 'laptop'].sample(n=1)

# Create a new DataFrame with the selected item
new_df = pd.DataFrame({
    'model': [random_pc['model'].values[0] + '_' + random_printer['model'].values[0],
              random_laptop['model'].values[0] + '_' + random_printer_2['model'].values[0]],
    'price': [random_pc['price'].values[0] + random_printer['price'].values[0],
              random_laptop['price'].values[0] + random_printer_2['price'].values[0]],
    'type': ['pc_printer', 'laptop_printer']
})

# Reduce the summed prices by 10%
new_df['price'] = new_df['price'] * 0.9

print(new_df)
# Print the resulting DataFrame
# print(df[['model', 'type', 'profitability_index']])

# Close the database connection
conn.close()
