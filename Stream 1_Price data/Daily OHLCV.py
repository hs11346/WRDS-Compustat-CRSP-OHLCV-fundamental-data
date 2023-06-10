import os
os.environ['OPENBLAS_NUM_THREADS'] = "1"
import wrds
import pandas as pd
import numpy as np
import sqlite3
conn = wrds.Connection()
secprd = conn.raw_sql("""
                     select datadate,gvkey,iid,tic,exchg,cusip,conm,PRCOD,PRCHD,PRCLD,PRCCD,TRFD,CSHTRD
                     from comp_na_daily_all.secd
                     where datadate >= '2016-01-01' and datadate <= '2022-12-31'


                     """, 
                     date_cols=['datadate'])
print('Data imported succesfully')
conn.close()
secprd.columns = ['date', 'gvkey','iid', 'tic', 'exchg','cusip', 'conm', 'open', 'high', 'low',
       'close', 'total_return', 'volume']

#exchange code is the International Stock Exchange Codes (for Compustat / WRDS)
secprd.date = secprd.date.dt.date
secprd.exchg = secprd.exchg.astype('Int64')

secprd.to_csv('/home/hku/u3594016/ResearchBase/03_Dataset/daily_ohlcv.csv')