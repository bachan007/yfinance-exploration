from dividend_analysis import dividend_history_analysis
import pandas as pd
import os
import datetime as dt
import yfinance as yf
from nse_listed_companies import get_info

# df = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()),'files/my_stocks_watch.csv'))

# desired information list --> can be updated according to the requirements
info_list = ['symbol','longName','currentPrice','fiftyTwoWeekHigh','fiftyTwoWeekLow','dayHigh','dayLow','fiveYearAvgDividendYield','sector','website','industry','category']
# symbol='TECHM'


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
    df = (pd.DataFrame.from_dict(dic)).T
    df.reset_index(inplace=True)
    df.columns=['Index','Values']
    print(f"{symbol} Information \n{df}")
    
    return df

if __name__=="__main__":
    company_info_to_table("TECHM")




