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



# options = webdriver.ChromeOptions()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')






#Temporary Username: MCTEMP-D6DX7
#Temporary Password: S-EE98D098

text_file = open("flights.txt", "w",encoding="utf-8")  # out

driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
#driver.get ("https://tsdr.uspto.gov/documentviewer?caseId=sn86964477&docId=NFIN20160720")


with open('xmlapps2019.txt', encoding='latin-1') as f:  #in

    sreader=csv.reader(f, delimiter=' ', quotechar='"')
    for row in sreader:

        sn=str(row[1])
        dte=str(row[2])

        pdflink = str(row)
        pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn"+sn+"&docId=NFIN"+dte



        pdflink=pdflink.replace("\/","")
        pdflink = pdflink.replace("[", "")
        pdflink = pdflink.replace("]", "")
        pdflink = pdflink.replace("'", "")

        #driver.get("https://tsdr.uspto.gov/documentviewer?caseId=sn86964477&docId=NFIN20160720")

        driver.get(pdflink)
        chk=driver.page_source
        if "There is no" in chk:
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=OOA" + dte
            driver.get(pdflink)

        clickit =login_form = driver.find_element_by_id('download')
        clickit.click()
        time.sleep(2)
        #driver.close()


