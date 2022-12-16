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
    # plt.show()
    plt.savefig(f"Plots/{title}.png")
    print(f"{title} saved in Plots directory")
    
def dividend_history_analysis(ticker,export=False,save_plots=False):
    '''
    This function analyses the dividend history of the company.
    To downlaod the data enable epxport : 
    export=True
    To save the plots of the dividend performance of the company enable save_plots:
    save_plots=True
    '''
    try:
        # creating a ticker object
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
    
            # Printing the analysis
            print(f"{ticker} has given highest dividend of INR{max_dividend} on {max_dividend_date}")
            print(f"{ticker} has given a total dividend of INR{np.round(total_dividend,3)} from {dividend_df['Date'][0]} till {dividend_df['Date'][len(dividend_df)-1]}")
            print(f"{ticker} has given maximum dividend of INR{max_dividend_yearwise} in the Year {max_dividend_year}\n")
    
            # plotting the graphs
            if save_plots:
                directory='Plots'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print(f"{directory} created to save the plots")
                barplot(dividend_df.Date,dividend_df.Dividends,title=f"Datewise Dividend History of {ticker}")
                barplot(dividend_year.index,dividend_year.Dividends,title=f"Yearwise Dividend History of {ticker}")
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
# dividend_history_analysis('TECHM.NS',export=True,save_plots=True)

# for the list of companies
list_of_tickers = ['TECHM.NS','CAMPUS.NS','VEDL.NS',
'AMBUJACEM.NS','DHAMPURSUG.NS','DLF.NS',
'ICICIBANK.NS','RENUKA.NS','TRIVENI.NS',
'CDSL.NS','TATAPOWER.NS','TATAMOTORS.NS','ZOMATO.NS','WIPRO.NS']

for tickers in list_of_tickers:
    dividend_history_analysis(tickers,save_plots=True)


