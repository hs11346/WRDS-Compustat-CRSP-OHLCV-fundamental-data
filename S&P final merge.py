import os
os.environ['OPENBLAS_NUM_THREADS'] = "1"
import pandas as pd
import numpy as np

ohlcv = pd.read_csv('/home/hku/u3594016/ResearchBase/03_Dataset/daily_ohlcv.csv')
sp500 = pd.read_csv('/home/hku/u3594016/ResearchBase/03_Dataset/sp500_hist.csv')
fin_ratio = pd.read_csv('/home/hku/u3594016/ResearchBase/03_Dataset/fin_ratio.csv')
ind = pd.read_csv("/home/hku/u3594016/ResearchBase/03_Dataset/industry_class.csv")

sp500 = sp500.rename(columns = {"liid":'iid'})
ohlcv = ohlcv[ohlcv.gvkey.isin(list(sp500.gvkey.unique()))]
df = pd.merge(ohlcv,sp500,on=['gvkey','iid'])
df = df[df.date <= df.ending][df.date >= df.start][df.date <= df.linkenddt][df.date >= df.linkdt]

df = df[['date', 'gvkey', 'iid','permno','tic', 'exchg','conm', 'open', 'high',
       'low', 'close', 'total_return', 'volume', 'linkprim']]
df['month'] = df.date.apply(lambda x: x[0:7])

df = pd.merge(df,fin_ratio,how='inner',on=['gvkey','month'])
df2 = pd.merge(df,ind,how='inner',on='gvkey')
df2 = df2[df2.date <= df2.indthru][df2.date >= df2.indfrom]

df2.to_csv('/home/hku/u3594016/ResearchBase/03_Dataset/s&p_complete_file.csv')