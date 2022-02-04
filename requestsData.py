import requests
import pandas as pd
import numpy as np
import requests
import datetime

# date ='20210309'
# stock_no = '2330'
# url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s'%(date,stock_no)
# r = requests.get(url)
# r.text

# data = r.json()
# data

# def get_stock_histor(date, stock_no):
#     quotes = []
#     url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s'%(date,stock_no)
#     r = requests.get(url)
#     data = r.json()
#     return transform(data['data'])


date1 ='20210309'
url1 = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=%s&type=ALLBUT0999"%(date1)

# ["1101","台泥","7,858,213","6,316","368,020,594","46.70","47.00","46.55","46.85","<p style= color:red>+<\u002fp>","0.05","46.85","30","46.90","31","13.74"],

r = requests.get(url1)
r.text

data = r.json()
print(data)