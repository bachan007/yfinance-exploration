from dividend_analysis import dividend_history_analysis
import pandas as pd
import os
import yfinance as yf
from nse_listed_companies import get_info

# df = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()),'files/my_stocks_watch.csv'))

# desired information list --> can be updated according to the requirements
info_list = ['symbol','longName','currentPrice','fiftyTwoWeekHigh','fiftyTwoWeekLow','dayHigh','dayLow','fiveYearAvgDividendYield','sector','website','industry','category']

def company_info_to_table(symbol,index_symbol='NS'):
    company = yf.Ticker(f'{symbol}.{index_symbol}')
    company_info = company.info
    dic = {}
    for ele in info_list:
        dic[ele]=[company_info[ele]]
    face_value = get_info('FACE VALUE',symbol)
    dic['Face Value']=face_value
    df = pd.DataFrame.from_dict(dic)
    print(df.T)

company_info_to_table('TECHM')
