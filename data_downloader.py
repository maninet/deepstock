import json
from threading import Semaphore
from urllib.request import urlretrieve
import os

os.makedirs('data', exist_ok=True)

URL1 = 'http://quotes.money.163.com/service/chddata.html?code='
URL2 = '&start=19901231&end=20200515&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
with open('code.json', 'r') as f:
    code_name = json.load(f)
print(len(code_name.keys()))

def download_csv():
    for code in code_name.values():
        if code.startswith('6'):
            URL = URL1 + '0' + code + URL2
        else:
            URL = URL1 + '1' + code + URL2
        try:
            urlretrieve(URL, os.path.join('data', code +'.csv'))
            print(code, 'has been downloaded')
        except Exception as e:
            print(e)

sem = Semaphore(100)
def downloadsem():
    with sem:
        download_csv()

if __name__ == "__main__":
    downloadsem()

