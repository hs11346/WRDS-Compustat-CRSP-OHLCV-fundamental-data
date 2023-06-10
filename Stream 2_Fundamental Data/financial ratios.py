import wrds
import pandas as pd
import numpy as np

conn = wrds.Connection()

fin_ratio = conn.raw_sql("""
                        select *
                        from wrdsapps_finratio_ibes.firm_ratio_ibes
                        where adate >= '2022-01-01'


                        """, 
                     date_cols=['public_date'])
print('Data imported succesfully')
fin_ratio = fin_ratio.drop(['adate','qdate','ffi5_desc', 'ffi5', 'ffi10_desc',
       'ffi10', 'ffi12_desc', 'ffi12', 'ffi17_desc', 'ffi17', 'ffi30_desc',
       'ffi30', 'ffi38_desc', 'ffi38', 'ffi48_desc', 'ffi48', 'ffi49_desc',
       'ffi49'],axis = 1)
conn.close()
fin_ratio = fin_ratio.rename(columns={'public_date':'month'})
fin_ratio.month = fin_ratio['month'].dt.to_period('M')
fin_ratio.gvkey = fin_ratio.gvkey.astype(int)
fin_ratio.permno = fin_ratio.permno.astype(int)
fin_ratio.to_csv("/home/hku/u3594016/ResearchBase/03_Dataset/fin_ratio.csv")