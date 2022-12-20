# this is the script where multiple options will be provided for data to be taken

from data_to_pdf import info_to_pdf
from company_info import company_info_to_table
from dividend_analysis import dividend_history_analysis
from data_to_pdf import info_to_pdf


symbol='TECHM'

def stock_info(symbol,to_pdf=False,to_email=False,receiver_email=None):
    '''
    This function will provide the information regarding the stock and give the option either to get the
    information locally or export the info into pdf, set to_pdf=True
    Or send the pdf over email address, set to_email=True and give receiver's email id
    Email functionality is under process.
    '''
    if not to_pdf:
        company_info_to_table(symbol)
        dividend_history_analysis(symbol,save_plots=True)
        print("To get this data into PDF format set to_pdf=True")
    if to_pdf:
        info_to_pdf(company_info_to_table(symbol),symbol)
        print("To get this data into PDF format over email set to_pdf=True and to_email=True and provide email")

if __name__=="__main__":
    stock_info(symbol,to_pdf=True)
    