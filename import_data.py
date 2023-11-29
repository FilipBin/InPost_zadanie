import support
import pandas as pd

import sqlite3

connection = sqlite3.connect(support.path_database)
for table in support.tables_names:
    df = pd.read_csv(support.path + table + ".csv", delimiter=";")
    df.to_sql(name=table, con=connection, if_exists="append", index=False)
    # print(df)

