"""
@author: alex
"""

from collections import Counter
import pandas as pd
import numpy as np



def make_lookup_table(df_events):
    # find the unique number of events
    __tmp_lst = list(df_events['name'])    
    # this will give how many times each event type has found in the db
    __lst_events_freq = Counter(__tmp_lst)      
    __set_of_events = set(__tmp_lst)        
    print("There are ",len(__set_of_events)," number of different event types.")
    # make flat event list
    __flat_eventTypelist = [item for sublist in __set_of_events for item in sublist]
    # get values of column dataframe
    __tmp_int_list = df_events['object_id'].apply(int)
    __idx = __tmp_int_list.values
    # convert dataframe column 'post_id' 
    __tmp_lst = list(df_events['object_id'])    
    # create df with indexes set to be the post IDs and create a tmp df col
    new_df_events = pd.DataFrame(index = __idx, data = __tmp_lst)
    # print(list(__set_of_events))
    # create column labels of the dataframe with the corresponding event types
    new_df_events = pd.concat([new_df_events,pd.DataFrame(columns = list(__set_of_events))])    
    # set name for first col
    new_df_events=new_df_events.rename(columns = {0:'object_id'})
    # delete first df column 'post-id'
    del new_df_events['object_id']    
    # fill dataframe with zeros
    new_df_events[:] = 0              
    __lst_eventtype = df_events['name'].tolist()
    j = 0
    for index, row in new_df_events.iterrows():
        for i,c in enumerate(new_df_events.columns):
            if c == __lst_eventtype[j]: 
                new_df_events.set_value(index,c,1) 
        j = j + 1
    
    # print(new_df_events)
    #verification
    __res = new_df_events[new_df_events!=0].stack()
    # print(__res)
    
    
    
    return new_df_events, list(__set_of_events)
    

