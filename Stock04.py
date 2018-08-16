import requests
from bs4 import BeautifulSoup

class NSE:

    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_code)
        response = requests.get(self.stock_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.data_array = soup.find(id='responseDiv').getText().strip().encode('utf-8').split(":")

    def stock_latest_price(self):
        for item in self.data_array:
            if 'lastPrice' in item:
                index = self.data_array.index(item)+1
                latestPrice=self.data_array[index].split('"')[1]
                return float(latestPrice.replace(',',''))

    def company_name(self):
        for item in self.data_array:
            if 'companyName' in item:
                index = self.data_array.index(item)+1
                companyName=self.data_array[index].split('"')[1]
                return companyName

NSE_ABB = NSE("MIRZAINT")

print NSE_ABB.stock_url
print NSE_ABB.stock_latest_price()
print NSE_ABB.stock_code+" - "+NSE_ABB.company_name()
