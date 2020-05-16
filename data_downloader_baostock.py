import baostock as bs
import pandas as pd
from threading import Semaphore
import os

os.makedirs('datawithall', exist_ok=True)


def data_downloader(start_date, end_date):
    bs.login()

    stock_rs = bs.query_all_stock(end_date)
    stock_df = stock_rs.get_data()

    for code in stock_df['code']:
        print('Downloading' + code)
        k_rs = bs.query_history_k_data_plus(
            code,
            'date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST',
            start_date=start_date,
            end_date=end_date,
            frequency='d',
            adjustflag='2')
        data_df = pd.DataFrame(k_rs.get_data())
        data_df.to_csv(os.path.join('datawithall', code+'.csv'), encoding='utf-8', index=False)

    bs.logout()

sem = Semaphore(100)
def download_sem(start_date, end_date):
    with sem:
        data_downloader(start_date, end_date)

if __name__ == "__main__":
    download_sem('1990-01-01', '2020-05-15')