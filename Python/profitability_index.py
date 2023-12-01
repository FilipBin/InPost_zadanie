# Properties
# ==========
# OBJECT NAME: profitability_index
# DESCRIPTION: this file is to calculate profitability index

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# 2023-11-29    FB      branch1     Code formatting and removing drop tables statements
# ==========    ======  =======     ========================================================

from sqlalchemy import create_engine, text
import pandas as pd
from orm_models import Product, Laptop, PC, Printer
from support import path_database
from save_dataframe_to_csv import save_df_to_csv


class ProfitabilityIndexCalculator:

    def __init__(self):
        # Create the engine
        self.engine = create_engine(path_database, echo=True)


    def calculate_profitability_index(self):
        """
        calculate the profitability index
        :return:
        """
        with self.engine.connect() as connection:
            # Use SQLAlchemy text to execute the query
            query = '''
                SELECT p.model, p.type, ((l.ram + l.hd) / l.price) * l.speed AS profitability_index
                FROM product p
                JOIN laptop l 
                ON p.model = l.model
            '''

            # Execute the query and fetch results into a DataFrame
            df = pd.read_sql_query(query, connection)

            # Save the DataFrame to a CSV file
            save_df_to_csv(df, "profitability_index_v2.csv")