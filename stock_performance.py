import yfinance as yf
import datetime as dt
import datetime
import matplotlib.pyplot as plt
from base_scripts import date_format
import seaborn as sns
from base_scripts import line_graph,till_date,up_or_down
import numpy as np

import warnings
warnings.filterwarnings("ignore")


symbol='TECHM'
index_symbol='NS'
ticker = f"{symbol}.{index_symbol}"
# print(ticker)
# start_date = date_format('1-1-2022')
# end_date = date_format(dt.datetime.today().strftime('%Y-%m-%d'))

# data = yf.download(ticker,start_date,end_date)
# data.sort_index(ascending=False, inplace=True)
# print(start_date,end_date)
# print(data.head())

# plt.figure(figsize=(12,7))
# sns.lineplot(data.index,data['Adj Close'])
# plt.title(f"{ticker} average price movement from {start_date} to {end_date}")
# plt.xlabel('date')
# plt.ylabel('price in INR')
# plt.show()

date_list=till_date()
date_list_declaration=[
    '1 Week Before till Date',
    '1 Month Before till Date',
    '1 Quarter Before till Date',
    '1 Year Before till Date'
]
# df = yf.download(ticker,month_before,current_date)
# print(df['Adj Close'].tail(1)[0],df['Adj Close'].head(1)[0])
# line_graph(df.index,df['Adj Close'])
# print(up_or_down(df['Adj Close'].head(1)[0],df['Adj Close'].tail(1)[0]))
# # df = yf.download(ticker,year_before,current_date)
# # line_graph(df.index,df['Adj Close'])
# yf.download()


def adj_price_analysis(ticker,start_date,end_date,graph_declaration=None):

    data = yf.download(ticker,start_date,end_date)
    x,y=data.index,data['Adj Close']
    dt1=date_format(x[0])
    dt2=date_format(x[-1])
    change_per=up_or_down(y[0],y[-1])
    analysis = f"{ticker} is {change_per} between date ranging from {dt1} on Price INR {np.round(y[0],2)} to {dt2} on Price INR {np.round(y[1],2)}"
    print(analysis)
    line_graph(x,y,title=f"{graph_declaration} line graph for {ticker} ranging from {dt1} to {dt2}")

def analysis_on_multiple_times(ticker='TECHM.NS'):
    # analysis for YTD
    for i in range(len(date_list[1:])):
        adj_price_analysis(ticker,date_list[i+1],date_list[0],graph_declaration=date_list_declaration[i])



analysis_on_multiple_times('TECHM.NS')