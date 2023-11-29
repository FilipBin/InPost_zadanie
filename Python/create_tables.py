# Properties
# ==========
# OBJECT NAME: create_tables
# DESCRIPTION: this file is to create tables with relationships

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# 2023-11-29    FB      branch1     Code formatting and removing drop tables statements
# ==========    ======  =======     ========================================================

import sqlite3
import support


def create_tables():
    connection = sqlite3.connect(support.path_database)
    for sql in support.create_tables:
        connection.execute(sql)
    connection.commit()
    connection.close()