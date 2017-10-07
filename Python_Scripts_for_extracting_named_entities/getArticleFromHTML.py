"""
@author: alex
"""
from downloadHTML import *
import os
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import NavigableString

#this command can be put in comments if there is a need to run only this script  
os.system('downloadHTML.py')

final_clean_df_wp_posts = pd.read_csv('/home/alex/DFs_Saved_to_CSVs/final_clean_df_wp_posts.csv')


def strip_tags(html, invalid_tags):
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.findAll(True):
        if tag.name in invalid_tags:
            s = ""
            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(str(c), invalid_tags)
                s += str(c)
            tag.replaceWith(s)
    return soup



def extractAllTags(lst_letters):
    
    s_list = []

    
    invalid_tags = ['b', 'i', 'u', 'em']
    
    for idx, letters in enumerate(lst_letters):
        
        soup = BeautifulSoup(str(letters), "lxml")
        
        
        for match in soup.findAll('span'):
            match.unwrap()
        
        soup = strip_tags(str(soup), invalid_tags)
        
       
        anchors = soup.findAll('a')
        
        for anchor in anchors:
            anchor.replaceWithChildren()
    
        for script in soup.find_all('script'):
            script.extract()
      
        for d in soup.findAll('time'):
            d.decompose()


        paragraphs = soup.find_all('p')
        
        
        s = []
        for paragraph in paragraphs:
            s.append(paragraph.get_text(strip=False))
            
        
        s_tmp = " ".join(s)
        
        s = s_tmp.replace('[', '').replace(']', '').replace('/', '').replace('\t', '').replace('#', '').replace('{', '').replace('}', '').replace('|', '').replace('–', '').replace('*Invalid email address', '').replace('\n', '')
        
        s_list.append(s)
        
    
    return s_list



lst_letters = [None]*len(final_clean_df_wp_posts)


for index, row in final_clean_df_wp_posts.iterrows():
    lst_letters[index] = BeautifulSoup(row['beaut_soup_of_source_link'],"lxml").find_all("p")

# print(lst_letters[0])

# create new column 'letters_p' in dataframe
final_clean_df_wp_posts['letters_p'] = lst_letters

s_list = extractAllTags(lst_letters)

final_clean_df_wp_posts['text_of_articles'] = s_list

final_clean_df_wp_posts.to_csv('/home/alex/DFs_Saved_to_CSVs/final_clean_df_wp_posts_with_articleText.csv', sep=',', encoding='utf-8')

print(final_clean_df_wp_posts)  
  
