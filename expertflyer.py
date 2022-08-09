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
import pdfminer
from pdfminer.high_level import extract_text
import os
import time

#serereressfdfsdfsfsf

# options = webdriver.ChromeOptions()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')


#Temporary Username: MCTEMP-D6DX7
#Temporary Password: S-EE98D098
text_file = open("notfound.txt", "a",encoding="utf-8")  # out
text_file = open("notfound.txt", "a",encoding="utf-8")  # out
text_file = open("notfound.txt", "a",encoding="utf-8")  # out

driver = webdriver.Chrome(r'chromedriver.exe')
#driver.get ("https://tsdr.uspto.gov/documentviewer?caseId=sn86964477&docId=NFIN20160720")


with open('lefttorun.txt', encoding='latin-1') as f:  #in

    sreader=csv.reader(f, delimiter=' ', quotechar='"')
    for row in sreader:

        sn=str(row[0])
        dte=str(row[1])

#rrrwerewrereerere
        pdflink = str(row)
        pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn"+sn+"&docId=NFIN"+dte

        if sn.startswith('79'):  # for 79 marks
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=MNFFR" + dte #march 2022


        #pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn88538284&docId=NFIN20191209135017#docIndex=1&page=1"

        pdflink = pdflink.replace("\/", "")
        pdflink = pdflink.replace("\/", "")
        pdflink=pdflink.replace("\/","")
        pdflink = pdflink.replace("[", "")
        pdflink = pdflink.replace("]", "")
        pdflink = pdflink.replace("'", "")

        #driver.get("https://tsdr.uspto.gov/documentviewer?caseId=sn86964477&docId=NFIN20160720")

        driver.get(pdflink)
        time.sleep(2)
        chk=driver.page_source
        print (chk)
        if "There is no" in chk:
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=OOA" + dte
            driver.get(pdflink)
            time.sleep(2)
            chk = driver.page_source

        if "There is no" in chk:
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=PAT" + dte
            driver.get(pdflink)
            time.sleep(2)
            chk = driver.page_source


        if "There is no" in chk:
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=EAP" + dte
            driver.get(pdflink)
            time.sleep(2)
            chk = driver.page_source

        if "There is no" in chk:
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=PROA" + dte
            driver.get(pdflink)
            time.sleep(2)
            chk = driver.page_source

        if "There is no" in chk:
            if sn.startswith('79'): # for 79 marks
                pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=NFIN" + dte # march 2022
                driver.get(pdflink)
                time.sleep(2)
                chk = driver.page_source
        #add CEAP,MPRFR,mnfprn





        if "Error: Service Unavailable" in chk:
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=OOA" + dte
            driver.get(pdflink)
            time.sleep(2)
            chk = driver.page_source


        if "Error: Service Unavailable" in chk:
            pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=NFIN" + dte
            driver.get(pdflink)
            time.sleep(2)
            chk = driver.page_source

            #pdflink = "https://tsdr.uspto.gov/documentviewer?caseId=sn" + sn + "&docId=NFIN" + dte



#################### exp convert to text
        if "There is no" in chk:
            with open('notdone.txt', 'a') as the_file:
                the_file.write(sn+" "+dte)
                the_file.write('\n')

        else:
            clickit = driver.find_element_by_id('download')
            clickit.click()
        #try:
        #    time.sleep(1.5)
        #    htmldir = r'C:\Users\kofsk\Downloads'
        #    filename = sn+".pdf"
        #    fname = os.path.join(htmldir, filename)
        #    text = extract_text(fname)
        #    filename = sn + ".txt"
        #    fname = os.path.join(htmldir, filename)

         #   text_file=open(fname,"w",encoding="utf-8")
         #   text_file.write(text)
         #   text_file.close()
        #except:
        #    print (sn)


