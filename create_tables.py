import sqlite3

connection = sqlite3.connect('C:\\Users\\filip\\OneDrive\\Pulpit\\inpost zadanie\\DB_computers.db')

cursor = connection.cursor()

drop_table = "drop table if exists laptop"

cursor.execute(drop_table)

drop_table = "drop table if exists pc"

cursor.execute(drop_table)

drop_table = "drop table if exists printer"

cursor.execute(drop_table)

drop_table = "drop table if exists product"

cursor.execute(drop_table)

create_laptop =( """CREATE TABLE "laptop" 
                    (   "code"	INTEGER NOT NULL,
                    "model"	TEXT NOT NULL,
                    "speed"	INTEGER NOT NULL,
                    "ram"	INTEGER NOT NULL,
                    "hd"	INTEGER NOT NULL,
                    "price"	NUMERIC,
                    "screen"	INTEGER NOT NULL,
                    PRIMARY KEY("code") 
                    FOREIGN KEY(model) REFERENCES product(model)
                    )""")

create_pc = ( """CREATE TABLE "pc" 
                ( "code"	INTEGER NOT NULL,
                "model"	TEXT NOT NULL,
                "speed"	INTEGER NOT NULL,
                "ram"	INTEGER NOT NULL,
                "hd"	INTEGER NOT NULL,
                "cd"	TEXT NOT NULL,
                "price"	NUMERIC,
                PRIMARY KEY("code")
                 FOREIGN KEY(model) REFERENCES product(model)
                 )""")

create_printer = ( """
    CREATE TABLE "printer" (
	"code"	INTEGER NOT NULL,
	"model"	TEXT NOT NULL,
	"color"	TEXT NOT NULL,
	"type"	TEXT NOT NULL,
	"price"	NUMERIC,
	PRIMARY KEY("code")
	 FOREIGN KEY(model) REFERENCES product(model)
)"""

    )

create_product = ( """CREATE TABLE "product" (
	"maker"	TEXT NOT NULL,
	"model"	TEXT NOT NULL,
	"type"	TEXT NOT NULL,
	PRIMARY KEY("model") 
)
    
    """)

cursor.execute(create_laptop)
cursor.execute(create_pc)
cursor.execute(create_printer)
cursor.execute(create_product)