"""
@author: alex
"""
import csv
import pandas as pd
import numpy as np


def read_wp_posts():
    csvdbfile = "/home/alex/CSV_TablesDB/wp_posts.csv"
    with open(csvdbfile, "r") as f:
        reader = csv.reader(f, delimiter=',')
        my_list = list(reader)    
    f.close()
    return my_list


# remove the first lines (trash) from csv 
df_wp_posts = pd.DataFrame(read_wp_posts()).iloc[47:]


# give names to columns 
my_columns = ["ID", "post_author", "post_date", "post_date_gmt", "summary", "post_title", "post_excerpt", "post_status", "comment_status", "ping_status",
              "post_password", "newslines_post_name", "to_ping", "pinged", "post_modified", "post_modified_gmt", "post_content_filtered", "post_parent",
              "newslines_permalink", "menu_order", "post_type", "post_mime_type", "comment_count"]

# assign column names
df_wp_posts.columns = my_columns

# get new_df_wp_posts
new_df_wp_posts = df_wp_posts[['ID','post_date','post_title', 'summary','newslines_post_name','newslines_permalink']].copy()

# put np.nan where there is nothing and remove them 
new_df_wp_posts['summary'].replace('', np.nan, inplace=True)
new_df_wp_posts = new_df_wp_posts.dropna(how='any')

# create col for source links
new_df_wp_posts['source_link'] = None

# split to train 75% and test 25%
row_count = len(new_df_wp_posts)
split_point = int(row_count*1/1000)   
split_point = int(row_count*1/4)
test_data = new_df_wp_posts[:split_point]
train_data = new_df_wp_posts[split_point:]

# this can be change by user if he wants to run the train or test data
new_df_wp_posts = test_data   # train_data


# remove fields where source links were not found from the content-summary
def removeFromSourceLinks_NaN_values(new_df_wp_posts):
    new_df_wp_posts['source_link'].replace('', np.nan, inplace=True)
    clean_df_wp_posts = (new_df_wp_posts.dropna(how='any'))
    return clean_df_wp_posts

