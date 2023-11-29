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

import sqlite3
import pandas as pd
import support
import save_dataframe_to_csv


def calculate_profitability_index():
    connection = sqlite3.connect(support.path_database)
    df = pd.read_sql_query(support.query_to_calculate_profitability_index, connection)
    df['profitability_index'] = ((df['ram'] + df['hd']) / df['price']) * df['speed']
    final_df = df[['model', 'type', 'profitability_index']]
    save_dataframe_to_csv.save_df_to_csv(final_df, "profitability_index.csv")
    connection.close()