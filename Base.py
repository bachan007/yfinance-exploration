# This file contains the functions used by multiple files 
import matplotlib.pyplot as plt
import seaborn as sns
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