"""
@author: alex
"""

from extractValidData import *
from bs4 import BeautifulSoup
import os

os.system('extractValidData.py')

# convert all summaries to soups
def makeSummariesToSoups(new_df_wp_posts):    
    tmp_lst = []    
    for index, row in new_df_wp_posts.iterrows():
        tmp_lst.append(BeautifulSoup(row['summary'], "lxml"))    
    return tmp_lst



# get from list of soups the href > source link
def getFromSoupsTheSourceLinks(tmp_lst):
    list_of_sources = [None]*len(tmp_lst)
    for idx, obj in enumerate(tmp_lst):
        for a in obj.find_all('a', href=True):
            if a.text.strip():
                list_of_sources[idx] = a['href'] 
    return list_of_sources



# print only list of sources
def printListOfSources(list_of_sources):
    for source in list_of_sources:
        print(source)    
    

# fix .htm to .html
def FixHTM_to_HTML(clean_df_wp_posts):    
    # assign list_of_sources to temporary list
    tmp_lst = clean_df_wp_posts['source_link']    
    for index, row in enumerate(tmp_lst):
        if '.htm' in row:
            if '.html' in row:
                pass
            else: 
                tmp = row.replace('.htm','.html')
                clean_df_wp_posts['source_link'].iloc[index] = tmp    
    return clean_df_wp_posts
    


# call  makeSummariesToSoups()
tmp_lst = makeSummariesToSoups(new_df_wp_posts)

# call  getFromSoupsTheSourceLinks()
list_of_sources = getFromSoupsTheSourceLinks(tmp_lst)

# call  printListOfSources()
printListOfSources(list_of_sources)

# assign list of sources to dataframe column source_link
new_df_wp_posts['source_link'] = list_of_sources

# print complete df
print(new_df_wp_posts)

# get clean new_df_wp_posts
clean_df_wp_posts = removeFromSourceLinks_NaN_values(new_df_wp_posts)

# remove duplicates if needed
clean_df_wp_posts = clean_df_wp_posts.drop_duplicates(subset="source_link", keep="first")


# call FixHTM_to_HTML()
# print(clean_df_wp_posts['source_link'].iloc[0])
clean_df_wp_posts = FixHTM_to_HTML(clean_df_wp_posts)
#print(clean_df_wp_posts['source_link'].iloc[0])

# print complete clean df
print(clean_df_wp_posts)




