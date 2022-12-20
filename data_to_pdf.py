from fpdf import FPDF
from company_info import company_info_to_table
from dividend_analysis import dividend_history_analysis
import yfinance as yf
import datetime as dt
import os

# Margin
m = 20 
# Page width: Width of A4 is 210mm
pw = 210 - 2*m 
# Cell height
ch = 8

class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 8, "Header", 0, 1, 'C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

def info_to_pdf(df,symbol,index_symbol='NS'):
    company = yf.Ticker(f'{symbol}.{index_symbol}')
    company_info = company.info
    pdf = FPDF()
    pdf.set_margins(left=20,right=20,top=20)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(w=0, h=20, txt=company_info['longName'], ln=1)
    pdf.set_font('Arial', '', 16)
    pdf.cell(w=15, h=ch, txt="Date: ", ln=0)
    pdf.cell(w=10, h=ch, txt=f'{dt.date.today()}', ln=1)
    pdf.ln(ch)
    pdf.set_font('Arial','',12)
    pdf.multi_cell(w=0, h=5, txt=company_info['longBusinessSummary'])

    # Adding a new Page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(w=0, h=20, txt=f'Key Indicators : {symbol}', ln=1)
    pdf.ln(ch)
    # Table Header
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(w=60, h=ch, txt='Index', border=1, ln=0, align='C')
    pdf.cell(w=100, h=ch, txt='Values', border=1, ln=1, align='C')
    # Table contents
    pdf.set_font('Arial', '', 12)
    for i in range(0, len(df)):
        pdf.cell(w=60, h=ch, 
                txt=df['Index'].iloc[i], 
                border=1, ln=0, align='L')
        pdf.cell(w=100, h=ch, 
                txt=str(df['Values'].iloc[i]), 
                border=1, ln=1, align='R')

    # Setting the pages for dividend information
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(w=0, h=20, txt="Dividend Information", ln=1,align='C')
    try:
        image_list,dividend_analysis = dividend_history_analysis(symbol,save_plots=True,show_fig_only=False)
        for img in image_list:
            pdf.image(img, 
                x = None, y = None, w = 190, h = 0, type = 'PNG')
            pdf.ln(ch*2)     

        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(w=0, h=5, txt=dividend_analysis)

    except:
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(w=0, h=5, txt="No iformation Available")
    directory='PDFs'
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"{directory} created to save the plots")
    pdf.output(f'{directory}/{symbol}.pdf', 'F')
    print(f"\nData saved as : {directory}/{symbol}.pdf\n")

if __name__=="__main__":
    symbol='VEDL'
    info_data = company_info_to_table(symbol)
    info_to_pdf(info_data,symbol)