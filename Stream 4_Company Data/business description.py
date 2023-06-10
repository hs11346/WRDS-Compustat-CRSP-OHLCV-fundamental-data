import wrds
import pandas as pd
import numpy as np

conn = wrds.Connection()

desc = conn.raw_sql("""
                        select gvkey,busdescl
                        from comp_na_daily_all.co_busdescl
                        


                        """, 
                     )
print('Data imported succesfully')

desc.columns = ['gvkey','description']