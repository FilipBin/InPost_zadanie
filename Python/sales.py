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

from sqlalchemy import create_engine
import pandas as pd
from support import path_database
from save_dataframe_to_csv import save_df_to_csv
import support


class SalesCreator:

    def __init__(self):
        self.engine = create_engine(path_database, echo=True)

    def create_sales(self):
        """
        Create a sales offer from random pc & printer and random laptop & printer
        :param:self
        :return:csv file
        """
        with self.engine.connect() as connection:
            query = support.query_to_create_sale

            df_created_sales_offer = pd.read_sql_query(query, connection)
            df_created_sales_offer['price'] = pd.to_numeric(df_created_sales_offer['price'], errors='coerce')

            random_pc = df_created_sales_offer[df_created_sales_offer['type'] == 'pc'].sample(n=1)
            random_printer = df_created_sales_offer[df_created_sales_offer['type'] == 'printer'].sample(n=1)
            random_printer_2 = df_created_sales_offer[df_created_sales_offer['type'] == 'printer'].sample(n=1)
            random_laptop = df_created_sales_offer[df_created_sales_offer['type'] == 'laptop'].sample(n=1)

            df_created_offer_to_csv = pd.DataFrame({
                'model': [random_pc['model'].values[0] + '_' + random_printer['model'].values[0],
                          random_laptop['model'].values[0] + '_' + random_printer_2['model'].values[0]],
                'price': [random_pc['price'].values[0] + random_printer['price'].values[0],
                          random_laptop['price'].values[0] + random_printer_2['price'].values[0]],
                'type': ['pc_printer', 'laptop_printer']
            })
            df_created_offer_to_csv['price'] = df_created_offer_to_csv['price'] * 0.9
            save_df_to_csv(df_created_offer_to_csv, "sale_offer_v2.csv")