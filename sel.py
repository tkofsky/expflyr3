import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import csv
import re
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



# options = webdriver.ChromeOptions()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')




driver = webdriver.Chrome(r'chromedriver.exe')
driver.get ("http://tsdr.uspto.gov/")
appnum='90705900'
#aa=driver.find_element_by_id('searchNumber')
#aa.send_keys(appnum)
#aa.send_keys(Keys.ENTER)
#driver.execute_script(f"document.getElementById('searchNumber').setAttribute('value', '{appnum}')")
#driver.execute_script(f"document.getElementById('searchNumber').value=121212")
driver.execute_script(f"document.getElementById('searchNumber').value=121212")
aa = BeautifulSoup(driver.page_source, 'html.parser')

clickit = driver.find_element_by_id('statusSearch')
clickit.click()

#w2.document.getElementById("documentSearch").Click
#w2.document.getElementById("searchNumber").Value = appnum

driver.close()


