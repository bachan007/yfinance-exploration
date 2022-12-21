# This file contains the functions used by multiple files 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from dateutil import parser
import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def addlabels(x,y):
    '''Displays the values on bars'''
    for i in range(len(x)):
        plt.text(i, np.round(y[i],2), np.round(y[i],2), ha = 'center')


def barplot(x,y,title=None,Flag=True):
    plt.figure(figsize=(12,7))
    sns.barplot(x=x,y=y,palette='flare')
    addlabels(x,y)
    plt.xticks(rotation=90)
    plt.title(title)
    if Flag:
        plt.show()
    else:
        plt.savefig(f"Plots/{title}.png")
        img_path = f"Plots/{title}.png"
        print(f"{title} saved in Plots directory")
        return img_path

def line_graph(x,y,title=None,Flag=True):
    plt.figure(figsize=(12,7))
    sns.lineplot(x,y)
    plt.title(title)
    addlabels(x,y)
    plt.xticks(rotation=90)
    plt.title(title)
    if Flag:
        plt.show()
    else:
        plt.savefig(f"Plots/{title}.png")
        img_path = f"Plots/{title}.png"
        print(f"{title} saved in Plots directory")
        return img_path


def date_format(date_val):
    ''''
    This function parses the dates into the desired format
    '''
    try:
        date_val = parser.parse(date_val,dayfirst=True)
        formatted_date = date_val.strftime("%Y-%m-%d")
        return formatted_date
    except:
        return date_val.strftime('%Y-%m-%d')
    # if formatted_date:
    #     return formatted_date
    # else:
    #     print("Enter a valid Date")

def till_date():
    '''
    This function returns current date date before 1 month and date before 1 year
    '''
    current_date = dt.datetime.now()
    week_minus_one = current_date-relativedelta(weeks=1)
    month_minus_one = current_date-relativedelta(months=1)
    qtr_minus_one = current_date-relativedelta(months=3)
    year_minus_one = current_date-relativedelta(years=1)
    dates_list = [current_date,week_minus_one,month_minus_one,qtr_minus_one,year_minus_one]
    dates_list = [ele.strftime("%Y-%m-%d") for ele in dates_list]
    return dates_list

def up_or_down(val1,val2):
    val1,val2=np.round(val1,2),np.round(val2,2)
    if val1>val2:
        return f"Down by {np.round(((val1-val2)/val1)*100,2)}%"
    elif val1<val2:
        return f"Up by {np.round(((val2-val1)/val1)*100,2)}%"
    elif val1==val2:
        return "No Change"
