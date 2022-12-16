# This file contains the functions used by multiple files 
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


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