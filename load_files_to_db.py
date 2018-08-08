import numpy as np
import pandas as pd
from flask_app import flask_app, db
from flask_app.models import Nat_avg, School_details, Zip_to_latlong, Wiki_summary, Message


def load_nat_avg(row):
    nat_avg = Nat_avg(CCBASIC = row['CCBASIC'],
                    MN_EARN_WNE_P6 = row['MN_EARN_WNE_P6'],
                    DEBT_MDN = row['DEBT_MDN'],
                    C150_4_COMB = row['C150_4_COMB'],
                    COSTT4_COMB = row['COSTT4_COMB'],
                    WDRAW_ORIG_YR6_RT = row['WDRAW_ORIG_YR6_RT'],
                    NPT4_COMB = row['NPT4_COMB'],
                    PCTPELL = row['PCTPELL'],
                    RET_FT4_COMB = row['RET_FT4_COMB'],
                    RET_PT4_COMB = row['RET_PT4_COMB'],
                    ADJ_AVGFACSAL = row['ADJ_AVGFACSAL'],
                    ADJ_INEXPFTE = row['ADJ_INEXPFTE'],
                    PFTFTUG1_EF = row['PFTFTUG1_EF'],
                    PFTFAC = row['PFTFAC'],
                    COMB_RET_RATE = row['COMB_RET_RATE'])
    
    db.session.add(nat_avg)
    db.session.commit()

    return

    
    
def load_summary(row):
    summary = Wiki_summary(uid=row['uid'],
                            inst_nm = row['INSTNM'],
                            UNITID = row['UNITID'],
                            OPEID = row['OPEID'],                           
                            wiki_summary = row['wiki_summary'].decode('utf8'),
                            date_extracted = row['time_extracted'][:10],
                            wiki_url = row['wiki_url'],
                            FB_HANDL = row['FB_HANDL'][:98],
                            TW_HANDL = row['TW_HANDL'][:98]                           
                          )
    db.session.add(summary)
    db.session.commit()
    return

def load_zip_lat_long(row):

    loc = Zip_to_latlong(zip_code= row['zip_code'],
                         lat_ = row['latitude'],
                         long_ = row['longitude']
                        )    
    db.session.add(loc)
    db.session.commit()                         
    return
                         

def load_school_details(row):

    school_detail = School_details(uid=row['uid'],  
                                UNITID = row['UNITID'],                                   
                                OPEID = row['OPEID'],
                                OPEID6 = row['OPEID6'],
                                INSTNM = row['INSTNM'],
                                CITY = row['CITY'].decode('utf8'),
                                STABBR = row['STABBR'],
                                ZIP5 = row['ZIP5'],
                                PREDDEG = row['PREDDEG'],
                                HTTPS_INSTURL = row['HTTPS_INSTURL'],
                                HTTPS_NPCURL = row['HTTPS_NPCURL'],
                                HIGHDEG = row['HIGHDEG'],
                                CONTROL = row['CONTROL'],
                                REGION = row['REGION'],
                                LOCALE = row['LOCALE'],
                                LATITUDE = row['LATITUDE'],
                                LONGITUDE = row['LONGITUDE'],
                                CCBASIC = row['CCBASIC'],
                                CCUGPROF = row['CCUGPROF'],
                                CCSIZSET = row['CCSIZSET'],
                                SATVRMID = row['SATVRMID'],
                                SATMTMID = row['SATMTMID'],
                                SATWRMID = row['SATWRMID'],
                                ACTCMMID = row['ACTCMMID'],
                                ACTENMID = row['ACTENMID'],
                                ACTMTMID = row['ACTMTMID'],
                                ACTWRMID = row['ACTWRMID'],
                                POP_SUBS = row['POP_SUBS'],
                                SATVR25 = row['SATVR25'], 
                                SATVR75 = row['SATVR75'],
                                SATMT25 = row['SATMT25'],
                                SATMT75 = row['SATMT75'],
                                SATWR25 = row['SATWR25'],
                                SATWR75 = row['SATWR75'],
                                ACTCM25 = row['ACTCM25'],
                                ACTCM75 = row['ACTCM75'],
                                ACTEN25 = row['ACTEN25'],
                                ACTEN75 = row['ACTEN75'],
                                ACTMT25 = row['ACTMT25'],
                                ACTMT75 = row['ACTMT75'],
                                ACTWR25 = row['ACTWR25'],
                                ACTWR75 = row['ACTWR75'],                                
                                UGDS = row['UGDS'],
                                TUITIONFEE_IN = row['TUITIONFEE_IN'],
                                TUITIONFEE_OUT = row['TUITIONFEE_OUT'],
                                ADJ_ADM_RATE = row['ADJ_ADM_RATE'],
                                OTHER_AFFIL = row['OTHER_AFFIL'],
                                REL_AFFIL = row['REL_AFFIL'],
                                COUNT_MISSING = row['COUNT_MISSING'],
                                VALUE_INDEX = row['VALUE_INDEX'],
                                CARE_INDEX = row['CARE_INDEX'],
                                Value_score = row['Value_score'],
                                Care_score = row['Care_score'],                                   
                                r_fin_MN_EARN_WNE_P6 = row['r_fin_MN_EARN_WNE_P6'],
                                r_fin_DEBT_MDN = row['r_fin_DEBT_MDN'],
                                r_fin_C150_4_COMB = row['r_fin_C150_4_COMB'],
                                r_fin_COSTT4_COMB = row['r_fin_COSTT4_COMB'],
                                r_fin_WDRAW_ORIG_YR6_RT = row['r_fin_WDRAW_ORIG_YR6_RT'],
                                r_fin_NPT4_COMB = row['r_fin_NPT4_COMB'],
                                r_fin_PCTPELL = row['r_fin_PCTPELL'],
                                r_fin_RET_FT4_COMB = row['r_fin_RET_FT4_COMB'],
                                r_fin_RET_PT4_COMB = row['r_fin_RET_PT4_COMB'],
                                r_fin_ADJ_AVGFACSAL = row['r_fin_ADJ_AVGFACSAL'],
                                r_fin_ADJ_INEXPFTE = row['r_fin_ADJ_INEXPFTE'],
                                r_fin_PFTFTUG1_EF = row['r_fin_PFTFTUG1_EF'],
                                r_fin_PFTFAC = row['r_fin_PFTFAC'],
                                r_fin_COMB_RET_RATE = row['r_fin_COMB_RET_RATE'],
                                MN_EARN_WNE_P6_PRESENT = row['MN_EARN_WNE_P6_PRESENT'],
                                DEBT_MDN_PRESENT = row['DEBT_MDN_PRESENT'],
                                C150_4_COMB_PRESENT = row['C150_4_COMB_PRESENT'],
                                COSTT4_COMB_PRESENT = row['COSTT4_COMB_PRESENT'],
                                WDRAW_ORIG_YR6_RT_PRESENT = row['WDRAW_ORIG_YR6_RT_PRESENT'],
                                NPT4_COMB_PRESENT = row['NPT4_COMB_PRESENT'],
                                PCTPELL_PRESENT = row['PCTPELL_PRESENT'],
                                RET_FT4_COMB_PRESENT = row['RET_FT4_COMB_PRESENT'],
                                RET_PT4_COMB_PRESENT = row['RET_PT4_COMB_PRESENT'],
                                ADJ_AVGFACSAL_PRESENT = row['ADJ_AVGFACSAL_PRESENT'],
                                ADJ_INEXPFTE_PRESENT = row['ADJ_INEXPFTE_PRESENT'],
                                PFTFTUG1_EF_PRESENT = row['PFTFTUG1_EF_PRESENT'],
                                PFTFAC_PRESENT = row['PFTFAC_PRESENT'],
                                fin_COMB_RET_RATE_PRESENT = row['fin_COMB_RET_RATE_PRESENT'],
                                rankp_MN_EARN_WNE_P6 = row['rankp_MN_EARN_WNE_P6'],
                                rankp_DEBT_MDN = row['rankp_DEBT_MDN'],
                                rankp_C150_4_COMB = row['rankp_C150_4_COMB'],
                                rankp_COSTT4_COMB = row['rankp_COSTT4_COMB'],
                                rankp_WDRAW_ORIG_YR6_RT = row['rankp_WDRAW_ORIG_YR6_RT'],
                                rankp_NPT4_COMB = row['rankp_NPT4_COMB'],
                                rankp_PCTPELL = row['rankp_PCTPELL'],
                                rankp_ADJ_AVGFACSAL = row['rankp_ADJ_AVGFACSAL'],
                                rankp_ADJ_INEXPFTE = row['rankp_ADJ_INEXPFTE'],
                                rankp_PFTFAC = row['rankp_PFTFAC'],
                                rankp_COMB_RET_RATE = row['rankp_COMB_RET_RATE'],
                                adm_pct = row['adm_pct'],
                                IF_SAT_PRESENT = row['IF_SAT_PRESENT'],
                                IF_ACT_PRESENT = row['IF_ACT_PRESENT']                                
    
    )
    
    db.session.add(school_detail)
    db.session.commit()                         
    return    

if __name__ == '__main__':
    load_summary()
