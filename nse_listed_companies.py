'''
 In this script i am exploring a static file which can be downloaded from :
https://www1.nseindia.com/content/equities/EQUITY_L.csv
This file contains all the NSE listed companies information.
'''

import pandas as pd
import numpy as np
import os
from Base import barplot

equity_df = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()),'files/EQUITY_L.csv'))

# cleaning the column names 
def clean_columns(columns):
    clean_cols = [col.strip() for col in columns]
    return clean_cols
cleaned_cols = clean_columns(equity_df.columns.to_list())
equity_df.columns = cleaned_cols

equity_df['NAME OF COMPANY'] = equity_df['NAME OF COMPANY'].apply(lambda x : x.title().strip())
equity_df['SYMBOL'] = equity_df['SYMBOL'].apply(lambda x : x.upper().strip())
equity_df['DATE OF LISTING']=pd.to_datetime(equity_df['DATE OF LISTING'])
equity_df['YEAR OF LISTING']=equity_df['DATE OF LISTING'].dt.year
equity_df['MONTH OF LISTING']=equity_df['DATE OF LISTING'].dt.month_name()


def get_symbol(company_name):
    company_name=company_name.title().strip()
    temp_df=equity_df[equity_df['NAME OF COMPANY']==company_name]
    if temp_df.shape[0]!=0:
        sym = temp_df['SYMBOL'].values[0]
        return sym
    else:
        print('Data not Found')
        return None


def get_info(info_of,symbol):
    '''
    This function takes the symbol of company as input and returns the specific info of the company
    info_of can be ['NAME OF COMPANY','FACE VALUE','DATE OF LISTING','SERIES','PAID UP VALUE', 'MARKET LOT', 'ISIN NUMBER']
    '''
    symbol = symbol.strip().upper()
    temp_df=equity_df[equity_df['SYMBOL']==symbol]
    if temp_df.shape[0]!=0:
        info = temp_df[info_of].values[0]
        print(f'{info_of} of {symbol} is : {info}')
        return info
    else:
        print(f'{info_of} Data not Found for {symbol}')
        return None


def yearwise_count_of_listing():
    '''
    This function returns the number of companies listed in a particular year 
    '''
    yearwise_count = equity_df.groupby(['YEAR OF LISTING'])['SYMBOL'].count().reset_index()
    yearwise_count['Count of Companies'] = yearwise_count['SYMBOL']
    barplot(yearwise_count['YEAR OF LISTING'],yearwise_count['Count of Companies'])
    return None

if __name__ == '__main__':
    yearwise_count_of_listing()
