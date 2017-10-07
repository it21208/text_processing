"""
@author: alex
"""
from getArticleFromHTML import *
import os
import pandas as pd
import numpy as np
import nltk
nltk.download()
from nltk.tokenize import word_tokenize
#from nltk.parse import malt
from nltk.tag.stanford import StanfordNERTagger
#from nltk.metrics.scores import accuracy
#from nltk import pos_tag
from itertools import groupby

os.system('getArticleFromHTML.py')

final_clean_df_wp_posts = pd.read_csv('/home/alex/DFs_Saved_to_CSVs/final_clean_df_wp_posts_with_articleText.csv')


print(final_clean_df_wp_posts)


lst_classified_text = [None]*len(final_clean_df_wp_posts)

lst_filtered_classified_text_of_articles = [None]*len(final_clean_df_wp_posts)

st=StanfordNERTagger('/usr/share/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz','/usr/share/stanford-ner-2017-06-09/stanford-ner.jar',encoding='utf-8')

for index, row in final_clean_df_wp_posts.iterrows():
    tokenized_text = word_tokenize(row[10])
    classified_text = st.tag(tokenized_text)
    lst_classified_text[index] = classified_text
    # print(classified_text)
    
    
    s = []  
    for tag, chunk in groupby(classified_text, lambda x:x[1]):
        if tag != "O":
            s.append([" ".join(w for w, t in chunk),tag])
            #print(s)
        
    lst_filtered_classified_text_of_articles[index] = s

    
final_clean_df_wp_posts['classified_text_of_articles'] = lst_classified_text


final_clean_df_wp_posts['filtered_classified_text_of_articles'] = lst_filtered_classified_text_of_articles



# final_clean_df_wp_posts['text_of_articles'].fillna(np.nan,inplace=True)

final_clean_df_wp_posts = final_clean_df_wp_posts.dropna(how='any')

final_clean_df_wp_posts.drop('Unnamed: 0', axis=1, inplace=True)
final_clean_df_wp_posts.drop('Unnamed: 0.1', axis=1, inplace=True)

#actual_list_of_named_entities = [('Trump', 'PERSON'), ('Vidhi', 'PERSON') , ('in', 'O'), ('translation', 'O'), (':', 'O'), ('president', 'O'), ("'s", 'O'), ('mangled', 'O'), ('language', 'O'), ('stumps', 'O'), ('interpreters', 'O'), ('|', 'O'), ('US', 'LOCATION'), ('news', 'O'), ('|', 'O'), ('The', 'O'), ('Guardian', 'O'), ('Mumbai', 'LOCATION'), ('Translators', 'O'), ('describe', 'O'), ('grappling', 'O'), ('with', 'O'), ('Trump', 'PERSON'), ('’', 'O'), ('s', 'O'), ('mannerisms', 'O'), ('for', 'O'), ('an', 'O'), ('international', 'O'), ('audience', 'O'), (':', 'O'), ('‘', 'O'), ('We', 'O'), ('try', 'O'), ('to', 'O'), ('grasp', 'O'), ('the', 'O'), ('context', 'O'), (',', 'O'), ('but', 'O'), ('it', 'O'), ('’', 'O'), ('s', 'O'), ('so', 'O'), ('incoherent', 'O'), ('’', 'O'), ('Translators', 'O'), ('describe', 'O'), ('grappling', 'O'), ('with', 'O'), ('Trump', 'PERSON'), ('’', 'O'), ('s', 'O'), ('mannerisms', 'O'), ('for', 'O'), ('an', 'O'), ('international', 'O'), ('audience', 'O'), (':', 'O'), ('‘', 'O'), ('We', 'O'), ('try', 'O'), ('to', 'O'), ('grasp', 'O'), ('the', 'O')]

#lst_counter_tp = [0]*len(s)
#print(type(actual_list_of_named_entities[0][0]))
#for indexi, obji in enumerate(s):
#    for indexj, objj in enumerate(actual_list_of_named_entities) :
#        if " " not in obji[0]:
#            if (obji[0] in objj[0]):  # (obji[0] in objj[0]) or (objj[0] in obji[0])
#                print("True",obji[0],"-",objj[0])
#                lst_counter_tp[indexi] = lst_counter_tp[indexi] + 1
#        else:
#            tmp = obji[0].split()
#            for indexk, objk in enumerate(tmp):
#                if objk in objj[0]:
#                   print("True",obji[0],"-",objj[0])
#                   lst_counter_tp[indexi] = lst_counter_tp[indexi] + 1    
