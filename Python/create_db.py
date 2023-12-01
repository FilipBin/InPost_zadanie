from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from data_loader import DataLoader
from orm_models import Base, Product, Laptop, PC, Printer

class CreateDb:

    def __init__(self):
        """
        Creating database, truncating tables and loading data in to tables
        :param:self
        :return:
        """
        database_location = "sqlite:///../Database/DB_computers_v2.db"

        engine = create_engine(database_location, echo=True)

        session = sessionmaker(bind=engine)
        session = session()
        Base.metadata.create_all(bind=engine)
        session.commit()
        self.truncate_tables(session)
        data_loader = DataLoader(session)
        data_loader.load_data()
        session.commit()

    def truncate_tables(self, session):
        """
        It's checking if table already exists and truncate them if yes
        :param session:
        :return:
        """
        session.query(Product).delete()
        session.query(Laptop).delete()
        session.query(PC).delete()
        session.query(Printer).delete()