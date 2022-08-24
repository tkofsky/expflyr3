from bs4 import BeautifulSoup
import time
print ("xxxxxx")



import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities().FIREFOX
#caps["pageLoadStrategy"] = "none"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"
start = time.time()
driver = webdriver.Chrome(desired_capabilities=caps, executable_path=r'C:\Users\User\PycharmProjects\selenium\geckodriver.exe')

driver.get("http://airbnb.com")
source = driver.page_source
soup = BeautifulSoup(source)
print(soup.title)
print ("done")
print ("'%s\' fetched in %ss" % ("", (time.time() - start)))