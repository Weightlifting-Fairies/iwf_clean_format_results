#%%
import re
import math
import pandas as pd
import numpy as np
#from pandas import DataFrame, Series
# Note: must use str.contains for looking up data
# Use this module with the import_clean_results.py or only this if data is scraped directly from website

df = pd.read_csv('cleaned_results2019.csv', skiprows = 1, sep='\s*,\s*',
                 delimiter=',', encoding='ascii',
                 names=('pid', 'gender', 'rank', 'rank_s', 'rank_cj', 'name', 'born', 'nation', 'category', 'bweight',
                        'snatch1', 'snatch2', 'snatch3', 'snatch', 'jerk1', 'jerk2', 'jerk3', 'jerk', 'total', 'event', 'date'))
#%%




df['lname'] = df['name'].str.extract("(.*[A-Z]+(?:[A-Z]))")
df['fname'] = df['name'].str.extract("([A-Z](?=[a-z]).*|\s[A-Z](?=\.).*)")


print(df.iloc[223])
print(df.iloc[290])



#%%
