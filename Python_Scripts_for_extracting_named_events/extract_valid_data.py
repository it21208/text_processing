"""
@author: alex
"""
import csv
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

def read_wp_posts():
    __csv_db_file = "/home/alex/NewslinesNamedEventsPrediction/csv_tables_db/wp_posts.csv"
    with open(__csv_db_file, "r") as f:
        __reader = csv.reader(f, delimiter=',')
        __my_list = list(__reader)    
    f.close()
    return __my_list


def extract_clean_summary(new_df_wp_posts):
    for __idx, __row in new_df_wp_posts.iterrows():
        __soup = BeautifulSoup(__row['summary'], "lxml")
        
        for __a in __soup.findAll('a'):
            del __a['href']
        
        for __script in __soup.find_all('script'):
            __script.extract()
            
        __data = str(__soup)
        __p = re.compile(r'<.*?>')
        __clean_data = __p.sub('', __data)      
        __clean_data = __clean_data.replace('[', '').replace(']', '').replace('/', '').replace('\t', '').replace('#', '').replace('{', '').replace('}', '').replace('|', '').replace('–', '').replace('*Invalid email address', '').replace('\n', '')                                           
        __clean_data = re.sub(r'^https?:\/\/.*[\r\n]*', '', __clean_data, flags=re.MULTILINE)
        __clean_data = re.sub(r"http\S+", "", __clean_data)
        new_df_wp_posts.set_value(__idx,'summary',__clean_data)       
    return new_df_wp_posts



def extract_valid_data():
    # remove the first lines (trash) from csv 
    __df_wp_posts = pd.DataFrame(read_wp_posts()).iloc[47:]    
    # give names to columns 
    __my_columns = ["ID", "post_author", "post_date", "post_date_gmt", "summary", "post_title", "post_excerpt", "post_status", "comment_status", "ping_status",
                  "post_password", "newslines_post_name", "to_ping", "pinged", "post_modified", "post_modified_gmt", "post_content_filtered", "post_parent",
                  "newslines_permalink", "menu_order", "post_type", "post_mime_type", "comment_count"]    
    # assign column names
    __df_wp_posts.columns = __my_columns
    # get new_df_wp_posts
    __new_df_wp_posts = __df_wp_posts[['ID','post_date','post_title', 'summary','newslines_post_name','newslines_permalink']].copy()    
    # put np.nan where there is nothing and remove them 
    __new_df_wp_posts['summary'].replace("", np.nan, inplace=True)
    __new_df_wp_posts = __new_df_wp_posts.dropna(how='any')    
    __new_df_wp_posts2 = __new_df_wp_posts[['ID', 'summary']].copy()        
    __new_df_wp_posts2 = extract_clean_summary(__new_df_wp_posts2)        
    __new_df_wp_posts2.to_csv("/home/alex/NewslinesNamedEventsPrediction/csv_tables_db/wp_term_text_only.csv", sep=',', encoding='utf-8')    
    # split to train 75% and test 25%
    row_count = len(__new_df_wp_posts2)
    split_point = int(row_count*1/4)
    test_data = __new_df_wp_posts2[:split_point]
    train_data = __new_df_wp_posts2[split_point:]    
    # this can be change by user if he wants to run the train or test data
    # __new_df_wp_posts2 = train_data   #  test_data
    return __new_df_wp_posts2


