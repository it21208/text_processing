"""
@author: alex
"""
from extractURL import *
from bs4 import BeautifulSoup
import urllib.request
import os

os.system('extractURL.py')

clean_df_wp_posts['beaut_soup_of_source_link'] = ''

# geet HTML content of URLs by fetching
def getHTMLcontentOfURLs(clean_df_wp_posts):
    df_of_id_urls = clean_df_wp_posts[['ID','source_link']].copy()
    lst_url_soups = [None]*len(clean_df_wp_posts)    
    df_of_id_urls = df_of_id_urls.reset_index(drop=True)    
    for index, row in df_of_id_urls.iterrows():
        try:
            r = urllib.request.urlopen(row[1]).read()
            tmp_soup = BeautifulSoup(r, 'lxml')
            with open("/home/alex/HTML_downloads/"+str(row[0]), "w") as file:
                file.write(str(tmp_soup))
            print("The URL",row[1]," with post ID: ",row[0]," works")
            lst_url_soups[index] = [row[0],str(tmp_soup)]
        except:
            with open("/home/alex/HTML_links_that_dont_work/"+row[0], "w") as file:
                file.write(str(row[1]))
            print("The URL",row[1]," with post ID: ",row[0]," does not work")
    print("Done")
    return lst_url_soups


# geet HTML content of URLs by reading ready file - this requires that the scripts have been executed at least once and the 
# corresponding folders 'HTML_downloads' and 'HTML_links_that_dont_work' have been copied to 
# the folder 'not_to_delete_the_content_of_the_folders_inside'
def getReadyHTMLcontentOfURLs(clean_df_wp_posts):
    lst_url_soups = [None]*len(clean_df_wp_posts)
    lst = list(os.listdir('/home/alex/not_to_delete_the_content_of_the_folders_inside/HTML_downloads'))
    for obj_lst in enumerate(lst):
        with open('/home/alex/not_to_delete_the_content_of_the_folders_inside/HTML_downloads/'+obj_lst[1], 'r') as myfile:
            data=myfile.read().replace('\n', '')        
        lst_url_soups.append([obj_lst[1],data]) # str(tmp_soup)
    return lst_url_soups


# keep in the structure << clean_df_wp_posts >>  only the post IDs that worked 
def removelinksFrom_clean_df_wp_posts_ThatDontWork(clean_df_wp_posts):
    lst = list(os.listdir('/home/alex/HTML_links_that_dont_work'))
    for obj_lst in lst:
        for index, obj in clean_df_wp_posts.iterrows():
            if obj_lst == obj['ID']:
                clean_df_wp_posts = clean_df_wp_posts[clean_df_wp_posts['ID'] != obj_lst]
    return clean_df_wp_posts


def syncSoupsWith_clean_df_wp_posts(clean_df_wp_posts2,lst_url_soups):
    clean_lst_url_soups = [x for x in lst_url_soups if x != None]
    for obj_lst in clean_lst_url_soups:
        for index, obj in clean_df_wp_posts2.iterrows():
            if obj_lst[0] == obj['ID']:  
                clean_df_wp_posts2.set_value(index,'beaut_soup_of_source_link',obj_lst[1])
    return clean_df_wp_posts2


lst_url_soups = getHTMLcontentOfURLs(clean_df_wp_posts)
    
# lst_url_soups = getReadyHTMLcontentOfURLs(clean_df_wp_posts)

clean_df_wp_posts2 = removelinksFrom_clean_df_wp_posts_ThatDontWork(clean_df_wp_posts)

final_clean_df_wp_posts = syncSoupsWith_clean_df_wp_posts(clean_df_wp_posts2, lst_url_soups)

final_clean_df_wp_posts.to_csv('/home/alex/DFs_Saved_to_CSVs/final_clean_df_wp_posts.csv', sep=',', encoding='utf-8')
