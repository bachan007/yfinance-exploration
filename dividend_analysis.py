## Dividends info of Companies listed on NSE
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pandas as pd
import numpy as np
import os
import random
from nse_listed_companies import get_info, equity_df
from Base import barplot

import warnings
warnings.filterwarnings('ignore')

def date_format(dte):
    return dte.date().strftime('%Y-%b-%d')
        
def dividend_history_analysis(symbol,index_symbol='NS',export=False,save_plots=False):
    '''
    This function analyses the dividend history of the company.
    To downlaod the data enable epxport : 
    export=True
    To save the plots of the dividend performance of the company enable save_plots:
    save_plots=True
    '''
    try:
        # creating a ticker object
        ticker = f"{symbol}.{index_symbol}"
        tckr = yf.Ticker(ticker)
        dividend_series = tckr.dividends
        if len(dividend_series)==0:
            print(f'No Dividend Record found for {ticker}\n')
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

            company_name = get_info('NAME OF COMPANY',symbol)
            # Printing the analysis
            print(f"{company_name}({ticker}) has given highest dividend of INR{np.round(max_dividend,3)} on {max_dividend_date}")
            print(f"{company_name}({ticker}) has given a total dividend of INR{np.round(total_dividend,3)} from {dividend_df['Date'][0]} till {dividend_df['Date'][len(dividend_df)-1]}")
            print(f"{company_name}({ticker}) has given maximum dividend of INR{np.round(max_dividend_yearwise,3)} in the Year {max_dividend_year}\n")
    
            # plotting the graphs
            if save_plots:
                directory='Plots'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print(f"{directory} created to save the plots")
                barplot(dividend_df.Date,dividend_df.Dividends,title=f"Datewise Dividend History of {company_name}({ticker})")
                barplot(dividend_year.index,dividend_year.Dividends,title=f"Yearwise Dividend History of {company_name}({ticker})")
            if export:
                directory=f"Export/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print(f"{directory} Created to export the data\n")
                if not os.path.exists(f"Export/{ticker}.csv"):
                    dividend_df.to_csv(f"Export/{ticker}.csv",index=False)
                    print(f"Exported : Export/{ticker}.csv\n")
                else:
                    print(f'Data is already present for {ticker}\n')
    except Exception as e:
        print(f'Error Occured ...........\n{e}')     

# for a single company
# dividend_history_analysis('IOC',export=True,save_plots=True)
# dividend_history_analysis('IOC',save_plots=True)

# for the list of companies
# list_of_tickers = ['TECHM','CAMPUS','VEDL',
# 'AMBUJACEM','DHAMPURSUG','DLF',
# 'ICICIBANK','RENUKA','TRIVENI',
# 'CDSL','TATAPOWER','TATAMOTORS','ZOMATO','WIPRO']

# for tickers in list_of_tickers:
#     dividend_history_analysis(tickers,save_plots=True)


# Randomly selecting 10 companies and analysing the dividend history
symbol_list = equity_df['SYMBOL'].to_list()
random.shuffle(symbol_list)
for comp in symbol_list[0:10]:
    print(comp)
    dividend_history_analysis(comp,save_plots=True,export=True)
    print(comp)


