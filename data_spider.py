from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://quote.eastmoney.com/stock_list.html'

driver = webdriver.Chrome()
driver.get(URL)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "quotesearch"))
    )
    with open('data.txt', 'w') as f:
        f.write(element.text)

finally:
    driver.quit()