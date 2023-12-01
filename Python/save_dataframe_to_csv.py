# Properties
# ==========
# OBJECT NAME: save_dataframe_to_csv
# DESCRIPTION: this file is to save dataframe to csv file
# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# ==========    ======  =======     ========================================================

import support
import pandas as pd
import os


def save_df_to_csv(dataframe, filename):
    """
    create the output path by joining the csv directory and filename and save DataFrame to a csv file,
    print an error if the file creation fails
    :param dataframe:
    :param filename:
    :return:
    """
    df_to_be_loaded_to_csv = pd.DataFrame(dataframe)
    output_path = os.path.join(support.path_to_csv, filename)

    try:
        df_to_be_loaded_to_csv.to_csv(output_path, index=False)
        print(f"File '{filename}' successfully created at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"File '{filename}' could not be created.")#