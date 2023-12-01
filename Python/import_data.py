# Properties
# ==========
# OBJECT NAME: import_data
# DESCRIPTION: this file is to import data from csv files into tables

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# 2023-11-29    FB      branch1     Code formatting and removing drop tables statements
# ==========    ======  =======     ========================================================

import support
import pandas as pd
import sqlite3


def load_data():
    """
    Create loop to each tables and read data from csv files
    :return:
    """
    connection = sqlite3.connect(support.path_database)
    for table in support.tables_names:
        df = pd.read_csv(support.path_to_tables + table + ".csv", delimiter=";")
        df.to_sql(name=table, con=connection, if_exists="append", index=False)
    connection.commit()
    connection.close()