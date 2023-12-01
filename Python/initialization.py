from profitability_index import ProfitabilityIndexCalculator
from sales import SalesCreator
import create_db


def start():
    """
    Create a new database, calculate and print the profitability index using the instantiated object
    :return:
    """
    # create_tables.create_tables()
    # truncate_tables.truncate_tables()
    # import_data.load_data()
    # sales.create_sales()
    create_db.CreateDb()
    calculate_profitalibity_index = ProfitabilityIndexCalculator()
    calculate_profitalibity_index.calculate_profitability_index()
    # create_sale_offer = SalesCreator()
    # create_sale_offer.create_sales()