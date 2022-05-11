import sqlite3
import pandas as pd
import time
import numpy as np
import datetime
from dateutil.rrule import rrule, MONTHLY

from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

raw_data_path = '../raw-data/databases/'
agg_csv_path = '../agg-data/agg_csv/'

conn = sqlite3.connect(raw_data_path+"curr_udplatency6.db")

def process_month(start_date, end_date):
    print("Processing udplatency6 for "+start_date+" "+end_date, flush=True)
    df_months_curr = pd.read_sql_query("select * from curr_udplatency6 "
                        + " where dtime >= '"+ start_date +"' and dtime < '" + end_date + "'"
                       + ";", conn)
    if not df_months_curr.empty :
        df_months_curr['dtime'] = pd.to_datetime(df_months_curr['dtime']).dt.date

        avg_num = is_numeric_dtype(df_months_curr['rtt_avg'])
        min_num = is_numeric_dtype(df_months_curr['rtt_min'])
        max_num = is_numeric_dtype(df_months_curr['rtt_max'])
        std_num = is_numeric_dtype(df_months_curr['rtt_std'])
        succ_num = is_numeric_dtype(df_months_curr['successes'])
        fail_num = is_numeric_dtype(df_months_curr['failures'])
        
        print('Numeric check: rtt_avg=' + str(avg_num) + ', rtt_min=' + str(min_num) + ', rtt_max=' + str(max_num) + ', rtt_std=' + str(std_num) + ', successes=' + str(succ_num) + ', failures=' + str(fail_num), flush=True)
        
        if not avg_num:
            df_months_curr['rtt_avg'] = pd.to_numeric(df_months_curr['rtt_avg'], errors='coerce')
            
        if not min_num:
            df_months_curr['rtt_min'] = pd.to_numeric(df_months_curr['rtt_min'], errors='coerce')
            
        if not max_num:
            df_months_curr['rtt_max'] = pd.to_numeric(df_months_curr['rtt_max'], errors='coerce')
            
        if not std_num:
            df_months_curr['rtt_std'] = pd.to_numeric(df_months_curr['rtt_std'], errors='coerce')
            
        if not succ_num:
            df_months_curr['successes'] = pd.to_numeric(df_months_curr['successes'], errors='coerce')
            
        if not fail_num:
            df_months_curr['failures'] = pd.to_numeric(df_months_curr['failures'], errors='coerce')
        
        df_months_curr.dropna(inplace=True)

        df_months_curr = (df_months_curr.groupby(['unit_id', 'dtime', 'target', 'location_id'], as_index=False)
        .agg({'rtt_avg':'median', 'rtt_min':'median','rtt_max':'median', 'rtt_std':'median', 'successes':'sum', 'failures': 'sum'})
        .rename(columns={'rtt_avg':'med_rtt_avg', 'rtt_min':'med_rtt_min','rtt_max':'med_rtt_max',  'rtt_std':'med_rtt_std', 'successes':'sum_suc', 'failures':'sum_fail'}))
        
        df_months_curr = df_months_curr[['unit_id', 'dtime', 'target', 'location_id', 'med_rtt_avg', 'med_rtt_min', 'med_rtt_max', 'med_rtt_std', 'sum_suc', 'sum_fail']]
        df_months_curr.to_csv(agg_csv_path+"udplatency6/agg_udplatency6_" + start_date + ".csv", index=False, header=None)
        print('Finished udplatency6 for '+start_date, flush=True)

process_month("2018-09-01", "2018-10-01")
process_month("2018-10-01", "2018-11-01")
process_month("2018-12-01", "2019-01-01")
process_month("2019-01-01", "2019-02-01")
process_month("2019-02-01", "2019-03-01")
process_month("2019-03-01", "2019-04-01")
process_month("2019-04-01", "2019-05-01")
process_month("2019-05-01", "2019-06-01")
process_month("2019-06-01", "2019-07-01")
process_month("2019-07-01", "2019-08-01")
process_month("2019-08-01", "2019-09-01")
process_month("2019-09-01", "2019-10-01")
process_month("2019-10-01", "2019-11-01")
process_month("2019-11-01", "2019-12-01")
process_month("2019-12-01", "2020-01-01")

conn.close()