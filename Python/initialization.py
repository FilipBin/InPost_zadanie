import create_tables
import import_data
import sales
import truncate_tables
import profitability_index

def start():
    create_tables.create_tables()
    truncate_tables.truncate_tables()
    import_data.load_data()
    sales.create_sales()
    profitability_index.calculate_profitability_index()