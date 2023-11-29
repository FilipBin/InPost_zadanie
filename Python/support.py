# Properties
# ==========
# OBJECT NAME: support
# DESCRIPTION: this file is to keep used variables

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# 2023-11-29    FB      branch1     Code formatting and removing drop tables statements
# ==========    ======  =======     ========================================================

tables_names = ['laptop', 'pc', 'printer', 'product']

path_to_tables = '../Database/tables/'

path_database = '../Database/DB_computers.db'

path_to_csv = '../'

create_laptop = '''
    CREATE TABLE IF NOT EXISTS "laptop" 
    ("code"	INTEGER NOT NULL,
    "model"	TEXT NOT NULL,
    "speed"	INTEGER NOT NULL,
    "ram"	INTEGER NOT NULL,
    "hd"	INTEGER NOT NULL,
    "price"	NUMERIC,
    "screen"	INTEGER NOT NULL,
    PRIMARY KEY("code") 
    FOREIGN KEY(model) REFERENCES product(model)
    )'''

create_pc = '''
    CREATE TABLE IF NOT EXISTS "pc" 
    ( "code"	INTEGER NOT NULL,
    "model"	TEXT NOT NULL,
    "speed"	INTEGER NOT NULL,
    "ram"	INTEGER NOT NULL,
    "hd"	INTEGER NOT NULL,
    "cd"	TEXT NOT NULL,
    "price"	NUMERIC,
    PRIMARY KEY("code")
    FOREIGN KEY(model) REFERENCES product(model)
    )'''

create_printer = '''
    CREATE TABLE IF NOT EXISTS "printer" (
    "code"	INTEGER NOT NULL,
    "model"	TEXT NOT NULL,
    "color"	TEXT NOT NULL,
    "type"	TEXT NOT NULL,
    "price"	NUMERIC,
    PRIMARY KEY("code")
    FOREIGN KEY(model) REFERENCES product(model)
    )'''


create_product = '''
    CREATE TABLE IF NOT EXISTS "product" (
    "maker"	TEXT NOT NULL,
    "model"	TEXT NOT NULL,
    "type"	TEXT NOT NULL,
    PRIMARY KEY("model") 
    )'''

create_tables = [create_laptop, create_printer, create_pc, create_product]

query_to_create_sale = '''
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

query_to_calculate_profitability_index = '''
     SELECT p.model, p.type, l.speed, l.ram, l.hd, l.price 
     FROM laptop l
     JOIN product p ON l.model = p.model
     WHERE p.type = 'laptop'                                      
     UNION
     SELECT p.model, p.type, pc.speed, pc.ram, pc.hd, pc.price
     FROM pc
     JOIN product p ON pc.model = p.model
     WHERE p.type = 'pc';
     '''
