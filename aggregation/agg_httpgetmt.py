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

conn = sqlite3.connect(raw_data_path+"curr_httpgetmt.db")

def process_month(start_date, end_date):
    print("Processing httpgetmt for "+start_date+" "+end_date, flush=True)
    df_months_curr = pd.read_sql_query("select * from curr_httpgetmt "
                        + " where dtime >= '"+ start_date +"' and dtime < '" + end_date + "'"
                       + ";", conn)
    if not df_months_curr.empty :
        df_months_curr['dtime'] = pd.to_datetime(df_months_curr['dtime']).dt.date

        fetch_time_num = is_numeric_dtype(df_months_curr['fetch_time'])
        bytes_total_num = is_numeric_dtype(df_months_curr['bytes_total'])
        bytes_sec_num = is_numeric_dtype(df_months_curr['bytes_sec'])
        succ_num = is_numeric_dtype(df_months_curr['successes'])
        fail_num = is_numeric_dtype(df_months_curr['failures'])
        
        print('Numeric check: fetch_time=' + str(fetch_time_num) + ', bytes_total=' + str(bytes_total_num) + ', bytes_sec=' + str(bytes_sec_num) + ', successes=' + str(succ_num) + ', failures=' + str(fail_num), flush=True)
        
        if not fetch_time_num:
            df_months_curr['fetch_time'] = pd.to_numeric(df_months_curr['fetch_time'], errors='coerce')
            
        if not bytes_total_num:
            df_months_curr['bytes_total'] = pd.to_numeric(df_months_curr['bytes_total'], errors='coerce')
            
        if not bytes_sec_num:
            df_months_curr['bytes_sec'] = pd.to_numeric(df_months_curr['bytes_sec'], errors='coerce')
            
        if not succ_num:
            df_months_curr['successes'] = pd.to_numeric(df_months_curr['successes'], errors='coerce')
            
        if not fail_num:
            df_months_curr['failures'] = pd.to_numeric(df_months_curr['failures'], errors='coerce')
        
        df_months_curr.dropna(inplace=True)

        df_months_curr = (df_months_curr.groupby(['unit_id', 'dtime', 'target', 'location_id'], as_index=False)
       .agg({'fetch_time':'median', 'bytes_total':'median','bytes_sec':'median', 'successes':'sum', 'failures': 'sum'})
       .rename(columns={'fetch_time':'med_fetch_time', 'bytes_total':'med_bytes_total','bytes_sec':'med_bytes_sec', 'successes':'sum_suc', 'failures':'sum_fail'}))
        
        df_months_curr = df_months_curr[['unit_id', 'dtime', 'target', 'location_id', 'med_fetch_time', 'med_bytes_total', 'med_bytes_sec', 'sum_suc', 'sum_fail']]

        df_months_curr.to_csv(agg_csv_path+"httpgetmt/agg_httpgetmt_" + start_date + ".csv", index=False, header=None)
        print('Finished httpgetmt for '+start_date, flush=True)


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