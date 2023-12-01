import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Python.data_loader import DataLoader
from Python.orm_models import Base, Product, Laptop, PC, Printer
import pandas as pd
from decimal import Decimal

class TestDatabaseConnection(unittest.TestCase):
    """
    Unit test to verify if connection to database id establish correctly
    Unit test to check if the data type is loaded correctly into tables
    """

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_connect_to_database(self):
        connection = self.engine.connect()
        self.assertTrue(connection.closed == 0)
        connection.close()

    def test_load_data_into_tables(self):
        data_loader = DataLoader(self.session)

        product_data = {'maker': 'TestMaker', 'model': 'TestModel', 'type': 'TestType'}
        laptop_data = {'code': 1, 'model': 'TestModel', 'speed': 2, 'ram': 4, 'hd': 500, 'price': 1000.0, 'screen': 15}
        pc_data = {'code': 2, 'model': 'TestModel', 'speed': 2, 'ram': 4, 'hd': 500, 'cd': 'DVD', 'price': 800.0}
        printer_data = {'code': 3, 'model': 'TestModel', 'color': 'Black', 'type': 'Laser', 'price': 200.10}

        data_loader.load_product_data(pd.DataFrame([product_data]))
        data_loader.load_laptop_data(pd.DataFrame([laptop_data]))
        data_loader.load_pc_data(pd.DataFrame([pc_data]))
        data_loader.load_printer_data(pd.DataFrame([printer_data]))

        self.assertTrue(isinstance(self.session.query(Product).first().maker, str))
        self.assertTrue(isinstance(self.session.query(Laptop).first().speed, int))
        self.assertTrue(isinstance(self.session.query(PC).first().cd, str))
        self.assertTrue(isinstance(self.session.query(Printer).first().price, Decimal))



if __name__ == '_main_':
    unittest.main()