"""
@author: alex
"""
import csv
from extractNamedEntities import *
import pandas as pd
import numpy as np
import collections
import os
from collections import defaultdict
from collections import Counter
from collections import defaultdict
from pandas import *



os.system('extractNamedEntities.py')

def read_wp_terms_eventtypes():
    csvdbfile = "/home/alex/CSV_TablesDB/wp_terms_eventtypes.csv"
    with open(csvdbfile, "r") as f:
        reader = csv.reader(f, delimiter=',')
        my_list = list(reader)    
    f.close()
    return my_list


def writeListOfUniqueEventsToFile(lst_SetOfEvents):
    df = pd.DataFrame(lst_SetOfEvents, columns=["Events"])
    df.to_csv("/home/alex/eventtypes/post_event.csv", index=False)


def readEventtypesCSVtoList():
    with open('/home/alex/eventtypes/post_event.csv', "rt") as f:
        reader = csv.reader(f)
        eventTypelist = list(reader)
        return eventTypelist

def writeDictionaryToCSV(events_dictionary):
    with open('/home/alex/eventtypes/events_dictionary.csv', 'w') as f: 
        w = csv.DictWriter(f, events_dictionary.keys())
        w.writeheader()
        w.writerow(events_dictionary)

    
    
my_list = read_wp_terms_eventtypes()
df_terms_eventtypes = pd.DataFrame(my_list)

# give names to columns 
my_columns = ["ID", "post_id", "eventtype"]

# assign column names
df_terms_eventtypes.columns = my_columns

# get new_df_wp_posts
new_df_terms_eventtypes = df_terms_eventtypes[['post_id','eventtype']].copy()

# find the unique number of events
tmp_lst = list(new_df_terms_eventtypes['eventtype'])

# this will give how many times each event type has found in the db
lst_events_freq = Counter(tmp_lst) 
 
SetOfEvents = set(tmp_lst)


print("There are ",len(SetOfEvents)," number of different event types.")
writeListOfUniqueEventsToFile(list(SetOfEvents))

# convert dataframe column 'post_id' 
tmp_lst = list(new_df_terms_eventtypes['post_id'])

# read csv file with unique events
eventTypelist = readEventtypesCSVtoList()



# make flat event list
flat_eventTypelist = [item for sublist in eventTypelist for item in sublist]

# get values of column dataframe
idx = new_df_terms_eventtypes['post_id'].values

# create df with indexes set to be the post IDs and create a tmp df col
df_post_events = pd.DataFrame(index = idx, data = tmp_lst)

# create column labels of the dataframe with the corresponding event types
df_post_events = pd.concat([df_post_events,pd.DataFrame(columns=flat_eventTypelist)])

# set name for first col
df_post_events=df_post_events.rename(columns = {0:'post_id'})

# delete first df column 'post-id'
del df_post_events['post_id']

# fill dataframe with zeros
df_post_events[:] = 0


       
lst_eventtype = new_df_terms_eventtypes['eventtype'].tolist()

j = 0
for index, row in df_post_events.iterrows():
    for i,c in enumerate(df_post_events.columns):
        if c == lst_eventtype[j]: 
            df_post_events.set_value(index,c,1) 
    j = j + 1



# print(df_post_events)

# verification
res = df_post_events[df_post_events!=0].stack()
#print(res)


# 2nd list of values for events_dictionary
lst_of_cnt = [None]*len(df_post_events.columns)
for index, column in enumerate(df_post_events):
    lst_of_cnt[index] = sum(df_post_events[column])


# keys for events_dictionary
list_of_keys = list(range(1,len(df_post_events.columns)+1))

# 1rst list of values for events_dictionary
tmp_lst = list(df_post_events.columns)


# obtain partial view of a dictionary
# dict(islice(events_dictionary.iteritems(), 0, 2)) 
# dict(list(events_dictionary.items())[0:10])
events_dictionary = dict(zip(list_of_keys,zip(tmp_lst,lst_of_cnt)))

# find the total frequency number of all event occurences
total_event_occurences = sum(lst_of_cnt)

# data structure to store the probability of each event happening
lst_events_probabilities = [None] * len(events_dictionary)

for key, value in events_dictionary.items():
    lst_events_probabilities[key] = [key, value[0], value[1], value[1]/total_event_occurences]
    print("The probability of the event '"+value[0]+"' happening is ",value[1]/total_event_occurences)


writeDictionaryToCSV(events_dictionary)
