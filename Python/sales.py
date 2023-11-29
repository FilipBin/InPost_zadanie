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

import sqlite3
import pandas as pd
import support
import save_dataframe_to_csv


def create_sales():
    conn = sqlite3.connect(support.path_database)
    df = pd.read_sql_query(support.query_to_create_sale, conn)
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
    new_df['price'] = new_df['price'] * 0.9
    save_dataframe_to_csv.save_df_to_csv(new_df, "sale_offer.csv")

    conn.close()