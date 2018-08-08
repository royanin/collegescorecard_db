import os
from config import basedir
from flask_app import flask_app, db
from flask_app.models import Nat_avg, School_details, Zip_to_latlong, Wiki_summary, Message
import pandas as pd
import numpy as np
from load_files_to_db import load_nat_avg, load_school_details, load_summary, load_zip_lat_long



def load_emails():
    new_email = "royanin.qn@gmail.com"
    new_msg = Message(body="lajkasvnlkanlkjvnal jknv sn alkjn alkjvna lkj ",
                      email=new_email,
                      sender_type='High school student -- searching for college',
                        subscribed=False)
    print new_msg
    db.session.add(new_msg)
    db.session.commit()    

def load_files():

    #load national_averages
    nat_avg_df = pd.read_csv('data/grouped_mean_set234.csv')
    nat_avg_df.apply(load_nat_avg,axis=1)
    #Done loading nat_avg    

    #load school_details
    sch_details_df1 = pd.read_csv('data/set_234.csv', dtype={'UNITID': np.string_ ,
                            'OPEID': np.string_ ,
                            'OPEID6': np.string_ ,
                            'ZIP5': np.string_ },
                                )
    sch_details_df = sch_details_df1.where(pd.notnull(sch_details_df1), None)
    sch_details_df.apply(load_school_details,axis=1)
    #Done loading school_details


    #load wiki_social
    """
    I don't really understand why it's necessary to have the na_values and keep_default_na
    for wiki_social_df. The same trick of using df.where(pd.notnull(df),None) fails in this particular
    case with sqlalchemy raising IntegrityError for duplicate entry.
    """
    wiki_social_df = pd.read_csv('data/wiki_social.csv', quotechar = '"',
                                 dtype={'wiki_summary':np.unicode_,
                                       'UNITID': np.string_ },
                                 na_values='NULL',
                                 keep_default_na=False
                              )
    #wiki_social_df = wiki_social_df1.where(pd.notnull(wiki_social_df1), None)
    wiki_social_df.apply(load_summary,axis=1)
    #Done wiki_social
    
    #load zip_codes to lat_long
    zip_to_loc1 = pd.read_csv('data/zip_codes_states.csv',                           
                            dtype={'zip_code':np.unicode_})
    zip_to_loc = zip_to_loc1.where(pd.notnull(zip_to_loc1), None)
    zip_to_loc.apply(load_zip_lat_long,axis=1)

    #Done zip_codes to lat_long
        
    
    return


if __name__ == '__main__':
    db.create_all()
    #load_emails()
    load_files()
                       
