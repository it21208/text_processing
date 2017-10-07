"""
@author: alex
"""

import csv
import pandas as pd
import numpy as np

def read_wp_term_taxonomy():
    __csv_db_file = "/home/alex/NewslinesNamedEventsPrediction/csv_tables_db/wp_term_taxonomy.csv"
    with open(__csv_db_file, "r") as f:
        __reader = csv.reader(f, delimiter=',')
        __my_list = list(__reader)    
    f.close()
    return __my_list



def read_wp_terms():
    __csv_db_file = "/home/alex/NewslinesNamedEventsPrediction/csv_tables_db/wp_terms.csv"
    with open(__csv_db_file, "r") as f:
        __reader = csv.reader(f, delimiter=',')
        __my_list = list(__reader)    
    f.close()
    return __my_list



def merge_wp_term_taxonomy_and_read_wp_terms():
    # create dataframe for wp_term_taxonomy table
    df_wp_term_taxonomy = pd.DataFrame(read_wp_term_taxonomy())
    # give names to columns 
    __wp_term_taxonomy_columns = ["term_taxonomy_id", "term_id", "taxonomy", "description", "parent", "count"]
    # assign column names
    df_wp_term_taxonomy.columns = __wp_term_taxonomy_columns
    # get new_df_wp_posts
    new_df_wp_term_taxonomy = df_wp_term_taxonomy[['term_taxonomy_id','term_id','taxonomy']].copy()
#=============================================================================================================#
    df_wp_terms = pd.DataFrame(read_wp_terms())
    # give names to columns 
    __wp_terms_columns = ["term_id", "name", "slug", "term_group", "term_order"]
    # assign column names
    df_wp_terms.columns = __wp_terms_columns
    # get new_df_wp_posts
    new_df_wp_terms = df_wp_terms[['term_id','name']].copy()
    # join two dataframes on 'term_id' column
    df_wp_term_taxonomy_and_wp_terms = pd.merge(new_df_wp_term_taxonomy, new_df_wp_terms, on='term_id', how='outer')
    # verify that the merge was done correctly
    # df_wp_term_taxonomy_and_wp_terms.iloc[7738] # term_taxonomy_id = 10148, term_id = 10046, taxonomy = event, name = Birth
    # df_wp_term_taxonomy_and_wp_terms.iloc[1025] # term_taxonomy_id = 2335, term_id = 2282, taxonomy = category, name = Garth Brooks
    return df_wp_term_taxonomy_and_wp_terms





