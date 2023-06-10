import os
os.environ['OPENBLAS_NUM_THREADS'] = "1"
import wrds
import pandas as pd
import numpy as np

conn = wrds.Connection()

idx_sp500 = conn.raw_sql("""
                        select * from crsp_a_indexes.dsp500list a 
                        inner join (select * from crsp_a_ccm.ccmxpf_linktable) b 
                        on a.permno = b.lpermno
                        """
                     )
print('Data imported succesfully')
conn.close()
idx_sp500.permno = idx_sp500.permno.astype('Int64')
idx_sp500 = idx_sp500[['permno','start','ending','gvkey','liid', 'linkdt', 'linkenddt','linkprim']]
idx_sp500.linkenddt = idx_sp500.linkenddt.fillna('2022-12-30')
idx_sp500.to_csv('/home/hku/u3594016/ResearchBase/03_Dataset/sp500_hist.csv')