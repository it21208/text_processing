"""
@author: alex
"""
import os 
from extractAllEvents import *

os.system('extractAllEvents.py')

final_clean_df_wp_posts['event_type']  = ''

for index1, row1 in final_clean_df_wp_posts.iterrows():
    for index2, row2 in new_df_terms_eventtypes.iterrows():
        if row1[0] == row2[0]:
            final_clean_df_wp_posts.set_value(index1,'event_type',row2[1])
            
clean_df_wp_posts.to_csv("/home/alex/DFs_Saved_to_CSVs/output_of_ArticlesMakeRelationshipsEvents", sep=',', encoding='utf-8')
        
