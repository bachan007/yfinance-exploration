## Dividends info of Companies listed on NSE
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pandas as pd
import numpy as np
import os

import warnings
warnings.filterwarnings('ignore')

def date_format(dte):
    return dte.date().strftime('%Y-%b-%d')
    
def addlabels(x,y):
    '''Displays the values on bars'''
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

def barplot(x,y,title=None):
    plt.figure(figsize=(12,7))
    sns.barplot(x=x,y=y,palette='flare')
    addlabels(x,y)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.show()
    
def dividend_history_analysis(ticker):
    '''
    This function analyses the history of the company
    '''
    try:
        # creating a ticker object
        tckr = yf.Ticker(ticker)
        dividend_series = tckr.dividends
        if len(dividend_series)==0:
            print(f'No Dividend Record found for {ticker}')
        else:
            # history of the dividend
            dividend_df = dividend_series.to_frame().reset_index()
            max_dividend = dividend_series.max()
            max_dividend_date = (dividend_series[dividend_series==max_dividend].index[0]).date().strftime('%Y-%b-%d')
            dividend_df['Date'] = dividend_df['Date'].apply(date_format)
            dividend_df['Year'] = dividend_df['Date'].apply(lambda x : x.split('-')[0])
            dividend_df['Month'] = dividend_df['Date'].apply(lambda x : x.split('-')[1])
            total_dividend = dividend_df['Dividends'].sum()
    
            dividend_year = dividend_df.groupby(['Year']).sum()
            max_dividend_yearwise = dividend_year.max()[0]
            max_dividend_year = dividend_year[dividend_year['Dividends']==max_dividend_yearwise].index[0]
    
            # Printing the analysis
            print(f"{ticker} has given highest dividend of INR{max_dividend} on {max_dividend_date}")
            print(f"{ticker} has given a total dividend of INR{np.round(total_dividend,3)} from {dividend_df['Date'][0]} till {dividend_df['Date'][len(dividend_df)-1]}")
            print(f"{ticker} has given maximum dividend of INR{max_dividend_yearwise} in the Year {max_dividend_year}\n")
    
            # plotting the graphs
            barplot(dividend_df.Date,dividend_df.Dividends,title=f"Datewise Dividend History of {ticker}")
            barplot(dividend_year.index,dividend_year.Dividends,title=f"Yearwise Dividend History of {ticker}")
    except Exception as e:
        print(f'Error Occured ...........\n{e}')     


list_of_tickers = ['TECHM.NS','CAMPUS.NS','VEDL.NS','AMBUJACEM.NS']
for tickers in list_of_tickers:
    dividend_history_analysis(tickers)