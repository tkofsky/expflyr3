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
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
import time
import asyncio
import requests

from selenium import webdriver

###########################################
#from drivermobproxy import Server
import psutil
import time
import psutil

#for proc in psutil.process_iter():
    # check whether the process name matches
#    if proc.name() == "drivermob-proxy":
 #       proc.kill()

driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')



driver=webdriver.Chrome()

#first tab
#driver.get('http://dell.com')

#second tab
#driver.execute_script("window.open('about:blank', 'tab2');")
#driver.switch_to.window("tab2")
#driver.get('http://bing.com')

#third tab
#driver.execute_script("window.open('about:blank', 'tab3');")
#driver.switch_to.window("tab3")
#driver.get('http://cnn.com')


#exit ()

#proxy.new_har("google")
#driver.get("http://www.google.co.uk")
#print (proxy.har) # returns a HAR JSON blob

#server.stop()
#driver.quit()



#####################
#####################################################################################################

start = time.time()
async def main():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, requests.get, 'http://www.google.com')
    future2 = loop.run_in_executor(None, requests.get, 'http://www.google.co.uk')
    response1 = await future1
    response2 = await future2
    print(response1.text)
    print(response2.text)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#print ("***Elapsed Time: %s" % (time.time() - start))


start = time.time()
drivera = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
drivera.execute_async_script("window.location.href = 'http://www.amazon.com';")
driverb = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
driverc = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
driverd = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
drivere = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
#driverf = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
driverg = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
#driverh = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
#driveri = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
#driverj = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')







drivera.get ("http://apple.com")
print(psutil.cpu_percent(), " ****cpu")
driverb.get ("http://dell.com")
print(psutil.cpu_percent(), " ****cpu")
driverc.get ("http://apple.com")
driverd.get ("http://dell.com")
print(psutil.cpu_percent(), " ****cpu")
driver.get ("http://apple.com")
#driverf.get ("http://dell.com")
print(psutil.cpu_percent(), " ****cpu")
driverg.get ("http://apple.com")
#print(psutil.cpu_percent(), " ****cpu")
#driverh.get ("http://dell.com")
#print(psutil.cpu_percent(), " ****cpu")
#driveri.get ("http://apple.com")
#print(psutil.cpu_percent(), " ****cpu")
#driverj.get ("http://dell.com")


print ("***Elapsed Time: %s" % (time.time() - start))