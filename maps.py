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

drivera = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
drivera.get ("https://map.geo.admin.ch/?lang=en&selectedNode=&topic=inspire&layers=ch.astra.unfaelle-personenschaeden_alle,KML%7C%7Chttps:%2F%2Fpublic.geo.admin.ch%2FjrXgKjP7R_KiadHPVi9VXQ,ch.bafu.wasser-teileinzugsgebiete_40&bgLayer=ch.swisstopo.pixelkarte-farbe&layers_timestamp=99990101,,&E=2525364.63&N=1238779.01&zoom=1&catalogNodes=57,58")

time.sleep(2)

action = webdriver.ActionChains(drivera)
element = drivera.find_elements_by_xpath("//*[contains(text(), 'Flood alert map')]")
action.move_to_element(element[0])
action.perform()

action = webdriver.ActionChains(drivera)
element = drivera.find_elements_by_xpath("//*[contains(text(), 'Ammonium')]")
action.move_to_element(element[0])
action.perform()