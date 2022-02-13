import requests
import pandas as pd
import numpy as np
import requests
import datetime
import time
import random

class SQLError(BaseException):
    pass

def get_stockNo_histor(date, stock_no):
    # date ='20210309',stock_no = '2330'
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s'%(date,stock_no)
    r = requests.get(url) # r.text
    data = r.json()
    # print(pd.DataFrame(data['data'], columns = data['fields']))
    return(data['data'])


def get_stock_histor(date):
    # date ='20210309'
    url1 = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=%s&type=ALLBUT0999"%(date)
    r = requests.get(url1)
    # r.text
    #'證券代號', '證券名稱', '成交股數', '成交筆數', '成交金額',       '開盤價', '最高價', '最低價', '收盤價', '漲跌(+/-)',                    '漲跌價差', '最後揭示買價', '最後揭示買量', '最後揭示賣價', '最後揭示賣量', '本益比'
    # 0050       元大台灣50  25,312,461  27,821     3,593,629,562  142.60     142.80    141.20    142.30    <p style= color:red>+</p>      0.75       142.30         108            142.35         400            0.00
    stockdata = r.json()
    if stockdata['stat'] == '很抱歉，沒有符合條件的資料!':
        pass
    else:
        print(pd.DataFrame(stockdata['data9'], columns = stockdata['fields9'])) # data4
        print(stockdata['fields9'])
        for row in stockdata['data9']:
            # print(row) # to sql
            err = None
            if err != None :
                raise SQLError("stock SQL ERROR")
    

def today_stock():
    loc_dt = datetime.datetime.today() 
    
    time_del = datetime.timedelta(days=3) 
    loc_dt = loc_dt - time_del 
    # print(loc_dt.isoweekday())
    if loc_dt.isoweekday() < 6:
        loc_dt_format = loc_dt.strftime("%Y%m%d") # %H:%M:%S
        # print(loc_dt_format) 
        get_stock_histor(loc_dt_format)
        return loc_dt_format


def Init():
    loc_dt = datetime.datetime.today() 
    for i in range(1,365):
        time_del = datetime.timedelta(days=i) 
        new_dt = loc_dt - time_del 
        print(new_dt.isoweekday())
        if new_dt.isoweekday() <6 :
            new_dt_format = new_dt.strftime("%Y%m%d") # %H:%M:%S
            print(new_dt_format)
            t = random.randrange(1500,6000) # wait
            # print(t)
            time.sleep(t/1000)
            get_stock_histor(new_dt_format)


# print(today_stock())
Init()