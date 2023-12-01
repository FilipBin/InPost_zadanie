import os
import pandas as pd
from sqlalchemy.orm import Session

from Python.orm_models import Laptop, PC, Printer, Product


class DataLoader:
    def __init__(self, session: Session):
        self.session = session

    def load_data(self):
        """
        Set the path to database containing CSV files
        :param:self
        :return:
        """
        base_path = os.path.abspath('../Database/tables/')

        # Load data for Product
        product_path = os.path.join(base_path, 'product.csv')
        product_data = pd.read_csv(product_path, delimiter=';')
        self.load_product_data(product_data)
        self.session.commit()

        # Load data for Laptop
        laptop_path = os.path.join(base_path, 'laptop.csv')
        laptop_data = pd.read_csv(laptop_path, delimiter=';')
        self.load_laptop_data(laptop_data)

        # Load data for PC
        pc_path = os.path.join(base_path, 'pc.csv')
        pc_data = pd.read_csv(pc_path, delimiter=';')
        self.load_pc_data(pc_data)

        # Load data for Printer
        printer_path = os.path.join(base_path, 'printer.csv')
        printer_data = pd.read_csv(printer_path, delimiter=';')
        self.load_printer_data(printer_data)
        self.session.commit()

    def load_product_data(self, data):
        """
        Create a product object with attributes and load product data into the database.
        :param data:
        :return:
        """
        for _, row in data.iterrows():
            product = Product(maker=row['maker'], model=row['model'], type=row['type'])
            self.session.add(product)

    def load_laptop_data(self, data):
        """
        Create a Laptop object with attributes and load laptop data into the database
        :param data:
        :return:
        """
        for _, row in data.iterrows():
            laptop = Laptop(
                code=row['code'],
                model=row['model'],
                speed=row['speed'],
                ram=row['ram'],
                hd=row['hd'],
                price=row['price'],
                screen=row['screen']
            )
            laptop.product = self.session.query(Product).filter_by(model=row['model']).first()
            self.session.add(laptop)

    def load_pc_data(self, data):
        """
        Create a pc object with attributes and load pc data into the database
        :param data:
        :return:
        """
        for _, row in data.iterrows():
            pc = PC(
                code=row['code'],
                model=row['model'],
                speed=row['speed'],
                ram=row['ram'],
                hd=row['hd'],
                cd=row['cd'],
                price=row['price']
            )
            pc.product = self.session.query(Product).filter_by(model=row['model']).first()
            self.session.add(pc)

    def load_printer_data(self, data):
        """
        Create a printer object with attributes and load printer data into the database
        :param data:
        :return:
        """
        for _, row in data.iterrows():
            printer = Printer(
                code=row['code'],
                model=row['model'],
                color=row['color'],
                type=row['type'],
                price=row['price']
            )
            printer.product = self.session.query(Product).filter_by(model=row['model']).first()
            self.session.add(printer)