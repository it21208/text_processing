"""
@author: alex
"""

from load_wp_term_relationships import load_wp_term_relationships
from load_wp_term_taxonomy_and_wp_terms import merge_wp_term_taxonomy_and_read_wp_terms
from make_relationships_events import make_associations_between_dfs
from make_lookup_table import make_lookup_table
from extract_valid_data import extract_valid_data
from use_vectorizer import execute_use_vectorizer



def main():
    
    __new_df_wp_term_relationships = load_wp_term_relationships()
    # print(__new_df_wp_term_relationships)        
    
    __new_df_wp_term_taxonomy_and_wp_terms = merge_wp_term_taxonomy_and_read_wp_terms()
    # print(__new_df_wp_term_taxonomy_and_wp_terms)        
    
    __new_final_clean_df_wp_posts = make_associations_between_dfs(__new_df_wp_term_relationships,__new_df_wp_term_taxonomy_and_wp_terms) 
    __df_events = __new_final_clean_df_wp_posts[['object_id','taxonomy','name']].copy()
    # print(__df_events)    
    
    __df_events.to_csv("/home/alex/NewslinesNamedEventsPrediction/csv_tables_db/output1_of_main.csv", sep=',', encoding='utf-8')
    __new_df_events, __set_of_events = make_lookup_table(__df_events)
    __new_df_events.to_csv("/home/alex/NewslinesNamedEventsPrediction/csv_tables_db/output2_of_main.csv", sep=',', encoding='utf-8')
    __new_df_wp_posts = extract_valid_data()
 
    #__np_events = __new_df_events.values
    execute_use_vectorizer(__new_df_wp_posts, __df_events)

    
    
    
    
if __name__ == "__main__": main()