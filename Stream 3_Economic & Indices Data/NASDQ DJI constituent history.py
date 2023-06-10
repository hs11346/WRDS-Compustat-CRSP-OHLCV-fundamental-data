import wrds
import pandas as pd
import numpy as np

conn = wrds.Connection()

idx = conn.raw_sql("""
                        select a.from as start, a.thru as ending, a.gvkeyx, a.gvkey, a.iid, b.conm from comp_na_daily_all.idxcst_his a
                        
                        inner join (select gvkeyx, conm from comp_na_daily_all.idx_index) b 

                        on a.gvkeyx = b.gvkeyx


                        """, 
                     date_cols=['date'])
print('Data imported succesfully')
conn.close()

