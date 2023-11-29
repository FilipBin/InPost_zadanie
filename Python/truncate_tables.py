# Properties
# ==========
# OBJECT NAME: truncate_tables
# DESCRIPTION: this file is to truncate tables

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# ==========    ======  =======     ========================================================

import support
import sqlite3


def truncate_tables():
    connection = sqlite3.connect(support.path_database)
    for table in support.tables_names:
        sql = f'delete from {table}'
        connection.execute(sql)

    connection.commit()
    connection.close()