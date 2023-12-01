from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from data_loader import DataLoader
from orm_models import Base, Product, Laptop, PC, Printer
from sqlalchemy import MetaData

class CreateDb:

    def __init__(self):
        """
        Creating database, truncating tables and loading data in to tables
        :param:
        :return:
        """
        database_location = "sqlite:///../Database/DB_computers_v2.db"

        # Create the engine
        engine = create_engine(database_location, echo=True)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(bind=engine)
        session.commit()
        self.truncate_tables(session)
        data_loader = DataLoader(session)
        data_loader.load_data()
        self.check_data_loaded(session)
        session.commit()

    def truncate_tables(self, session):
        """
        It's checking if table already exists and truncate them if yes
        :param session:
        :return:
        """
        table_names = ['Product', 'Laptop', 'PC', 'Printer']
        inspector = inspect(session.bind)
        existing_tables = inspector.get_table_names()
        metadata = MetaData()

        for table_name in table_names:
            if table_name in existing_tables:
                # Reflect the table using the MetaData
                table = table(table_name, metadata, autoload_with=session.bind)

                # Issue the delete statement
                session.execute(table.delete())
                session.commit()
            else:
                print(f"Table {table_name} does not exist.")

    def check_data_loaded(self, session):
        """
        Check if data is loaded for each table
        :param self:
        :param session:
        :return:
        """

        if session.query(Product).count() == 0:
            print("Error: No data loaded for Product table.")
        else:
            print("Data loaded successfully for Product table.")

        if session.query(Laptop).count() == 0:
            print("Error: No data loaded for Laptop table.")
        else:
            print("Data loaded successfully for Laptop table.")

        if session.query(PC).count() == 0:
            print("Error: No data loaded for PC table.")
        else:
            print("Data loaded successfully for PC table.")

        if session.query(Printer).count() == 0:
            print("Error: No data loaded for Printer table.")
        else:
            print("Data loaded successfully for Printer table.")
