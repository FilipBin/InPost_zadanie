# Properties
# ==========
# OBJECT NAME: profitability_index
# DESCRIPTION: this file is to calculate profitability index
# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# 2023-11-29    FB      branch1     Code formatting and removing drop tables statements
# ==========    ======  =======     ========================================================

from sqlalchemy import create_engine
import pandas as pd
import support
from save_dataframe_to_csv import save_df_to_csv


class ProfitabilityIndexCalculator:

    def __init__(self):
        self.engine = create_engine(support.path_database, echo=True)


    def calculate_profitability_index(self):
        """
        calculate the profitability index
        :param:self
        :return:csv file
        """
        with (self.engine.connect() as connection):
            query = support.query_to_calculate_profitability_index
            df_profitability_index = pd.read_sql_query(query, connection)
            df_profitability_index['profitability_index'] = ((
                (df_profitability_index['ram'] + df_profitability_index['hd']) /
                df_profitability_index['price']
            ) * df_profitability_index['speed']).round(2)
            df_profitability_index_final = pd.DataFrame(df_profitability_index[['model', 'type', 'profitability_index']])
            save_df_to_csv(df_profitability_index_final, "profitability_index_v2.csv")
