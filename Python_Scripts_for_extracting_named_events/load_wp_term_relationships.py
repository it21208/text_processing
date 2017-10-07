"""
@author: alex
"""
import csv
import pandas as pd



def read_wp_term_relationships():
    _csvdbfile = "/home/alex/NewslinesNamedEventsPrediction/csv_tables_db/wp_term_relationships.csv"
    with open(_csvdbfile, "r") as f:
        _reader = csv.reader(f, delimiter=',')
        _my_list = list(_reader)    
    f.close()
    return _my_list


def load_wp_term_relationships():
    _df_wp_term_relationships = pd.DataFrame(read_wp_term_relationships())
    # give names to columns 
    _my_columns = ["object_id", "term_taxonomy_id", "term_order"]              
    # assign column names
    _df_wp_term_relationships.columns = _my_columns
    # get new_df_wp_posts
    _new_df_wp_term_relationships = _df_wp_term_relationships[['object_id','term_taxonomy_id']].copy()
    return _new_df_wp_term_relationships



