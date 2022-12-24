from dividend_analysis import dividend_history_analysis
import pandas as pd
import numpy as np
import os
import datetime as dt
import yfinance as yf
from nse_listed_companies import get_info

# df = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()),'files/my_stocks_watch.csv'))

# desired information list --> can be updated according to the requirements
info_list = ['symbol','longName','currentPrice','fiftyTwoWeekHigh','fiftyTwoWeekLow','dayHigh','dayLow','fiveYearAvgDividendYield','bookValue','sector','website','industry','category']
# symbol='TECHM'

def discount_percentage(fifty_two_week_high,price_today):
    return f'{np.round(((fifty_two_week_high-price_today)/fifty_two_week_high)*100,2)}%'

def up_from_52_week_low(fifty_two_week_low,price_today):
    return f'{np.round(((price_today-fifty_two_week_low)/fifty_two_week_low)*100,2)}%'

def company_info_to_table(symbol,index_symbol='NS'):
    '''
    This function return the dataframe table of the desired information.
    '''
    company = yf.Ticker(f'{symbol}.{index_symbol}')
    company_info = company.info
    dic = {}
    dic['Date']=dt.date.today()
    for ele in info_list:
        dic[ele]=[company_info[ele]]
    face_value = get_info('FACE VALUE',symbol)
    listing_date = get_info('DATE OF LISTING',symbol)
    dic['Face Value']=face_value
    dic['Date of Listing']=listing_date
    dic['Discount from 52 week high'] = discount_percentage(company_info['fiftyTwoWeekHigh'],company_info['currentPrice'])
    dic['Up from 52 week low'] = up_from_52_week_low(company_info['fiftyTwoWeekLow'],company_info['currentPrice'])
    df = (pd.DataFrame.from_dict(dic)).T
    df.reset_index(inplace=True)
    df.columns=['Index','Values']
    print(f"{symbol} Information \n{df}")
    
    return df

if __name__=="__main__":
    company_info_to_table("TECHM")




