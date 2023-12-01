# Properties
# ==========
# OBJECT NAME: sales
# DESCRIPTION: this file is to create sale offer for laptop & printer and pc & printer

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# 2023-11-29    FB      branch1     Code formatting and removing drop tables statements
# ==========    ======  =======     ========================================================
from sqlalchemy import create_engine, text
import pandas as pd
from support import path_database
from save_dataframe_to_csv import save_df_to_csv


class SalesCreator:

    def __init__(self):
        # Create the engine
        self.engine = create_engine(path_database, echo=True)

    def create_sales(self):
        """
        Create a sales offer from random pc & printer and random laptop & printer
        :return:
        """
        with self.engine.connect() as connection:
            # Use SQLAlchemy text to execute the query
            query = text('''
                SELECT model, price, type FROM your_table;  -- Replace 'your_table' with the actual table name
            ''')

            # Execute the query and fetch results into a DataFrame
            df = pd.read_sql_query(query, connection)

            # Clean and process the DataFrame
            df['price'] = pd.to_numeric(df['price'], errors='coerce')

            random_pc = df[df['type'] == 'pc'].sample(n=1)
            random_printer = df[df['type'] == 'printer'].sample(n=1)
            random_printer_2 = df[df['type'] == 'printer'].sample(n=1)
            random_laptop = df[df['type'] == 'laptop'].sample(n=1)

            new_df = pd.DataFrame({
                'model': [random_pc['model'].values[0] + '_' + random_printer['model'].values[0],
                          random_laptop['model'].values[0] + '_' + random_printer_2['model'].values[0]],
                'price': [random_pc['price'].values[0] + random_printer['price'].values[0],
                          random_laptop['price'].values[0] + random_printer_2['price'].values[0]],
                'type': ['pc_printer', 'laptop_printer']
            })

            # Adjust prices
            new_df['price'] = new_df['price'] * 0.9

            # Save the DataFrame to a CSV file
            save_df_to_csv(new_df, "sale_offer_v2.csv")

