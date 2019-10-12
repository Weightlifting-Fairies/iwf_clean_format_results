import re
import math
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

""" This module extracts the data using panda and 
    adds 3 more columns: last name, first name, and 
    sinclair total while deleting columns: name, event, and date

    Note: Use this module with the import_clean_results.py 
    or only this if data is scraped directly from website
"""

# Note: Must use str.contains for looking up data


df = pd.read_csv('cleaned_new_bw_2019.csv', skiprows = 1, sep='\s*,\s*',
                 delimiter=',', encoding='ascii',
                 names=('pid', 'gender', 'rank', 'rank_s', 'rank_cj', 'name', 'born', 'nation', 'category', 'bweight',
                        'snatch1', 'snatch2', 'snatch3', 'snatch', 'jerk1', 'jerk2', 'jerk3', 'jerk', 'total', 'event', 'date'))



# Splits name and adds individual last and first name columns
## Name must not have an apostrophe ' 
df['lname'] = df['name'].str.extract("(.*[A-Z]+(?:[A-Z]))")
df['fname'] = df['name'].str.extract("([A-Z](?=[a-z]).*|\s[A-Z](?=\.).*)")

#Deletes name column
df = df.drop(columns=['name'])

def trim_all_columns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

# Sinclair total calculations
def men_sinclair(bwt, total):
    # Sinclair constants for 2017-2020
    A_2020_M = 0.751945030
    b_2020_M = 175.508

    # Calculation
    quotient = bwt/b_2020_M
    X = np.log10(quotient)
    A_Xsq = A_2020_M * X**2
    S_coeff = 10**(A_Xsq)
    S_total = total * S_coeff
    return S_total


def women_sinclair(bwt, total):
    # Sinclair constants for 2017-2020
    A_2020_W = 0.783497476
    b_2020_W = 153.655

    # Calculation
    quotient = bwt/b_2020_W
    X = np.log10(quotient)
    A_Xsq = A_2020_W * X**2
    S_coeff = 10**(A_Xsq)
    S_total = total * S_coeff
    return S_total

df['bweight'] = pd.to_numeric(df['bweight'], errors='coerce')
df['total'] = pd.to_numeric(df['total'], errors='coerce')
df['sinclair_total'] = pd.np.where(df['gender'] == 'M', men_sinclair(df['bweight'], df['total']), women_sinclair(df['bweight'], df['total']))

df = trim_all_columns(df)

cols = list(df.columns.values)
df = df[['pid', 'gender', 'rank', 'rank_s', 'rank_cj', 'lname', 'fname', 'born', 'nation', 'category', 'bweight', 'snatch1', 'snatch2', 'snatch3', 'snatch', 'jerk1', 'jerk2', 'jerk3', 'jerk', 'total', 'event', 'date', 'sinclair_total']]

name_of_output_csv = " ".join([df['event'][1]] + [df['date'].astype(str)[1]]).replace(' ', '_').replace('.','_') + '.csv'
#df = df.drop(columns=['event'])
#df = df.drop(columns=['date'])
name_of_output_csv = 'cleaned_formatted_new_bw_2019' + '.csv'

df.to_csv(name_of_output_csv, index=False)




