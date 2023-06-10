import wrds
import pandas as pd
import numpy as np

conn = wrds.Connection()

df = conn.raw_sql("""
                        select *
                        from comp_na_daily_all.co_hgic

                        """, 
                     )
print('Data imported succesfully')

df.gvkey = df.gvkey.astype(int)
df.indthru = df.indthru.fillna('2022-12-30')
df.to_csv("/home/hku/u3594016/ResearchBase/03_Dataset/industry_class.csv")
