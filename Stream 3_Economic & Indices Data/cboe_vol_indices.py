import wrds
import pandas as pd
import numpy as np

conn = wrds.Connection()

cboe_vol = conn.raw_sql("""
                        select *
                        from cboe_all.cboe
                        where date >= '2023-01-01'


                        """, 
                     date_cols=['date'])
print('Data imported succesfully')
conn.close()

cboe_vol = cboe_vol[['date', 'vixo', 'vixh', 'vixl', 'vix',
       'vxno', 'vxnh', 'vxnl', 'vxn', 'vxdo', 'vxdh', 'vxdl', 'vxd']]

cboe_vol.columns = ['date', 'vix_open', 'vix_high', 'vix_low', 'vix_close',
       'vxn_open', 'vxn_high', 'vxn_low', 'vxn_close', 'vxd_open', 'vxd_high', 'vxd_low', 'vxd_close']
