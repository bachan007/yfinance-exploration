'''
 In this script i am exploring a static file which can be downloaded from :
https://www1.nseindia.com/content/equities/EQUITY_L.csv
This file contains all the NSE listed companies information.
'''

import pandas as pd
import numpy as np
import os

equity_df = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()),'files/EQUITY_L.csv'))

# cleaning the column names 
def clean_columns(columns):
    clean_cols = [col.strip() for col in columns]
    return clean_cols
cleaned_cols = clean_columns(equity_df.columns.to_list())
equity_df.columns = cleaned_cols

equity_df['NAME OF COMPANY'] = equity_df['NAME OF COMPANY'].apply(lambda x : x.title().strip())
equity_df['SYMBOL'] = equity_df['SYMBOL'].apply(lambda x : x.upper().strip())


def get_symbol(company_name):
    company_name=company_name.title().strip()
    temp_df=equity_df[equity_df['NAME OF COMPANY']==company_name]
    if temp_df.shape[0]!=0:
        sym = temp_df['SYMBOL'].values[0]
        return sym
    else:
        print('Data not Found')


def get_company_name(symbol):
    '''
    This function takes the symbol of company as input and returns the name of the company
    '''
    symbol = symbol.strip().upper()
    temp_df=equity_df[equity_df['SYMBOL']==symbol]
    if temp_df.shape[0]!=0:
        cn = temp_df['NAME OF COMPANY'].values[0]
        return cn
    else:
        print(f'Data not Found for {symbol}')
        return None


def get_face_value_and_listing_date(symbol):
    symbol = symbol.strip().upper()
    temp_df=equity_df[equity_df['SYMBOL']==symbol]
    if temp_df.shape[0]!=0:
        fv = temp_df['FACE VALUE'].values[0]
        ld = temp_df['DATE OF LISTING'].values[0]
        return fv,ld
    else:
        print('Data not Found')

