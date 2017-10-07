"""
@author: alex
"""
import numpy as np
import pandas as pd


def make_associations_between_dfs(new_df_wp_term_relationships,df_wp_term_taxonomy_and_wp_terms):
    # join the two dataframes: _new_df_wp_term_relationships and _new_df_wp_term_taxonomy_and_wp_terms, on 'term_taxonomy_id' column 
    df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms = pd.merge(new_df_wp_term_relationships, df_wp_term_taxonomy_and_wp_terms, on='term_taxonomy_id', how='left')
    # get rid of taxonomies with nav_menu and bp-email-type
    new_df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms = df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] != 'nav_menu']
    DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms = new_df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[new_df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] != 'bp-email-type']
    # split the dataframe according to values on the col 'taxonomy' so to seperate the named entities and named events
    entities_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms = new_df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[new_df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] != 'dpa_event']
    new_entities_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms = entities_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[entities_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] != 'event']
    events_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms = new_df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[new_df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] != 'link_category']
    new_events_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms = events_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[events_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] != 'category']
    return new_events_DF_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms

############################### Some usefull information #######################################################

# verify dataframe
# df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[8220:8226]
#  index of dataframe          object_id   term_taxonomy_id   term_id    taxonomy             name
#  8221                           17232               2335       2282     category       Garth Brooks
#  8222                           17232              10148       10046     event            Birth


# len(df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms) # Out[113]: 91158

# remove the records of the dataframe df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms whose values in column 'taxonomy'
# are equal with  'nav_menu' or 'bp-email-type'    


#  myset = set(df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'])
#  print(myset)  
# {'bp-email-type',  'category', 'dpa_event', 'event', 'link_category', 'nav_menu'}

# df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] == 'bp-email-type']
#
#      object_id term_taxonomy_id term_id       taxonomy   name 
#82957    158120            14589   14487  bp-email-type   activity-comment
#82958    158121            14590   14488  bp-email-type   activity-comment-author
#82959    158122            14591   14489  bp-email-type   activity-at-message
#82960    158123            14592   14490  bp-email-type   groups-at-message
#82961    158124            14593   14491  bp-email-type   core-user-registration
#82962    158125            14594   14492  bp-email-type   core-user-registration-with-blog 
#82963    158126            14595   14493  bp-email-type   friends-request
#82964    158127            14596   14494  bp-email-type   friends-request-accepted 
#82965    158128            14597   14495  bp-email-type   groups-details-updated
#82966    158129            14598   14496  bp-email-type   groups-invitation
#82967    158130            14599   14497  bp-email-type   groups-member-promoted
#82968    158131            14600   14498  bp-email-type   groups-membership-request
#82969    158132            14601   14499  bp-email-type   messages-unread
#82970    158133            14602   14500  bp-email-type   settings-verify-email-change
#82971    158134            14603   14501  bp-email-type   groups-membership-request-accepted
#82972    158135            14604   14502  bp-email-type   groups-membership-request-rejected

# df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms[df_wp_term_relationships_and_wp_term_taxonomy_and_wp_terms['taxonomy'] == 'nav_menu']    
# 
#      object_id term_taxonomy_id term_id  taxonomy         name  
#1165       4127              412     400  nav_menu  Footer menu
#1166       4128              412     400  nav_menu  Footer menu
#1167       4129              412     400  nav_menu  Footer menu
#1179       4272              412     400  nav_menu  Footer menu
#1180       4273              412     400  nav_menu  Footer menu
#1301       4847              456     441  nav_menu         Help
#1344       5155              456     441  nav_menu         Help
#1366       5261              456     441  nav_menu         Help
#64223    110378              456     441  nav_menu         Help
#65333    115294              456     441  nav_menu         Help
#81214    155285              456     441  nav_menu         Help
#88831    167379              456     441  nav_menu         Help
#88869    167464            15204   15102  nav_menu  Agency menu
#88870    167465            15204   15102  nav_menu  Agency menu    






