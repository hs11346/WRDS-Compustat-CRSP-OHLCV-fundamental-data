import wrds
import pandas as pd
import numpy as np

conn = wrds.Connection()

div = conn.raw_sql("""
                        select datadate,gvkey,iid,tic,exchg,cusip,anncdate,paydate,recorddate,div
                        from comp_na_daily_all.secd
                        where datadate >= '2023-01-01'


                        """, 
                     date_cols=['datadate'])
print('Data imported succesfully')
conn.close()
div.columns = ['date', 'gvkey','iid', 'tic', 'exchg','cusip','div_declaration_date','div_pay_date','div_record_date','div_per_share']
div.date = div.date.dt.date
div = div.dropna().drop(columns = ['date'])
#div.to_csv('/users/harry/Desktop/VSCODE_PROJ/ResearchBase/Dataset/US_EQ_DAILY_OHLCV.csv')