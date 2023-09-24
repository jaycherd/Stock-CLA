from datetime import date,timedelta
# from io import BytesIO
# import base64
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from typing import List, Tuple
import yfinance as yf


def get_specific_date(num_days_ago) -> (str,'numpy.float64'):
    day = (pd.Timestamp(date.today()) - timedelta(days=num_days_ago)).strftime("%Y-%m-%d")
    return day,mdates.datestr2num(day)


def create_image(symbol):
    start_date,start_date_num = get_specific_date(num_days_ago=366)
    end_date,end_date_num = get_specific_date(num_days_ago=1)
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    # Define the date format
    date_fmt = '%Y-%m-%d'  # e.g., 2023-09-22
    date_formatter = mdates.DateFormatter(date_fmt)
    # Get current axis and set the formatter
    plt.figure(figsize=(10,5))
    plt.xlim(start_date_num,end_date_num)
    plt.xticks(rotation=45)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(date_formatter)
    ax.xaxis.set_major_locator(mdates.MonthLocator())   
    plt.plot(stock_data['Close'], label='Close Price')
    xtick_locs = ax.get_xticks()
    ymin,ymax = ax.get_ylim()
    plt.vlines(x=xtick_locs,ymin=ymin,ymax=ymax, color='#D3D3D3', linestyles='dashed', alpha=0.5)
    plt.title(f'{symbol} Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    return
    # img = BytesIO()
    # plt.savefig(img, format='png')
    # img.seek(0)
    # return base64.b64encode(img.getvalue()).decode()

#start dates arr for, 1yr/3yr/5yr/10yr, dont need to return ends cus all will end same time
#all dates, returns list of tuples, List((string,float),...)
def generate_dates(num_days_arr: List[int]) -> List[Tuple[str,'numpy.float64']]:
    starts = []
    counter = 0
    for days_ago in num_days_arr:
        tmpdate = (pd.Timestamp(date.today()) - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        tmptuple = (tmpdate,(mdates.datestr2num(tmpdate)))
        starts.append(tmptuple)
    return starts

def generate_chart_data(symbol,starts,end_date) -> List[int]:
    data_arr = []
    for tuple in starts:
        stock_data = yf.download(symbol, start=tuple[0], end=end_date)
        data_arr.append(stock_data)
    return data_arr

#1yr, 3yr, 5yr, 10yr
def create_longterm_plots(symbol):
    titles = [f"{symbol} 1 YR",f"{symbol} 3 YR", f"{symbol} 5 YR", f"{symbol} 10 YR"]
    starts = generate_dates([365, 365*3, 365*5, 365*10])
    end_date,end_date_num = get_specific_date(num_days_ago=0)
    fig, axs = plt.subplots(2,2,figsize=(12,8))
    #fig = whole figure with all subs
    #axs is a 2d numpy arr with subplot axes, ea/ele array as one subplot, can index with row/col
    stock_data_arr = generate_chart_data(symbol,starts,end_date)
    # date_fmt = '%Y-%m-%d'  # e.g., 2023-09-22
    # date_formatter = mdates.DateFormatter(date_fmt)
    # ax = plt.gca()
    # ax.xaxis.set_major_formatter(date_formatter)
    # ax.xaxis.set_major_locator(mdates.MonthLocator())   
    counter = 0
    for i in range(2):
        for j in range(2):
            axs[i,j].plot(stock_data_arr[counter]['Close'], label='Close Price')
            axs[i,j].tick_params(labelrotation=45)
            axs[i,j].set_title(titles[counter])
            axs[i,j].set_xlabel('Date')
            axs[i,j].set_ylabel('Close Price (USD)')
            xtick_locs = axs[i,j].get_xticks()
            ymin,ymax = axs[i,j].get_ylim()
            axs[i,j].vlines(x=xtick_locs,ymin=ymin,ymax=ymax, color='#D3D3D3', linestyles='dashed', alpha=0.5)
            counter += 1
    # xtick_locs = ax.get_xticks()
    # ymin,ymax = ax.get_ylim()
    # plt.vlines(x=xtick_locs,ymin=ymin,ymax=ymax, color='#D3D3D3', linestyles='dashed', alpha=0.5)
    # plt.xlabel('Date')
    # plt.ylabel('Close Price (USD)')
    # plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

def create_medterm_plots(symbol):
    titles = [f"{symbol} 5 DAYS",f"{symbol} 10 DAYS", f"{symbol} 1 MONTH", f"{symbol} 6 MONTH"]
    starts = generate_dates([5,10,30,185])
    end_date,end_date_num = get_specific_date(num_days_ago=0)
    fig, axs = plt.subplots(2,2,figsize=(12,8))
    stock_data_arr = generate_chart_data(symbol,starts,end_date)
    counter = 0
    for i in range(2):
        for j in range(2):
            axs[i,j].plot(stock_data_arr[counter]['Close'], label='Close Price')
            axs[i,j].tick_params(labelrotation=45)
            axs[i,j].set_title(titles[counter])
            axs[i,j].set_xlabel('Date')
            axs[i,j].set_ylabel('Close Price (USD)')
            xtick_locs = axs[i,j].get_xticks()
            ymin,ymax = axs[i,j].get_ylim()
            axs[i,j].vlines(x=xtick_locs,ymin=ymin,ymax=ymax, color='#D3D3D3', linestyles='dashed', alpha=0.5)
            counter += 1

    plt.tight_layout()
    plt.show()
