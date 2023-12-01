from profitability_index import ProfitabilityIndexCalculator
from sales import SalesCreator
import create_db


def start():
    """
    Create a new database, calculate and print the profitability index using the instantiated object
    """
    create_db.CreateDb()
    calculate_profitalibity_index = ProfitabilityIndexCalculator()
    calculate_profitalibity_index.calculate_profitability_index()
    create_sale_offer = SalesCreator()
    create_sale_offer.create_sales()
