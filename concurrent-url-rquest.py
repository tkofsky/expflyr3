import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
from selenium import webdriver
from multiprocessing import Pool
import psutil
from time import time
from selenium import webdriver


url_list = [
    "https://www.dell.com/",
    "https://www.bing.com/",
    "https://www.apple.com/","https://www.salesforce.com/","https://www.cnbc.com/","https://www.microsoft.com/","https://www.tesla.com/","https://www.facebook.com/","https://www.matrox.com/","https://www.samsung.com/"]


def download_filex(url):
    html = requests.get(url, stream=True)
    soup = BeautifulSoup(html.text)
    print(soup.title)
    return html.status_code

start = time()

for url in url_list:
    print(download_filex(url))

print(f'Time taken: {time() - start}')


################################# same as above but with threads

url_list = [
    "https://www.dell.com/",
    "https://www.bing.com/",
    "https://www.apple.com/","https://www.salesforce.com/","https://www.cnbc.com/","https://www.microsoft.com/","https://www.tesla.com/","https://www.facebook.com/","https://www.matrox.com/","https://www.samsung.com/"]#,"https://www.nvidia.com/",]

def download_file(url):
    html = requests.get(url, stream=True)

    soup = BeautifulSoup(html.text)

    print(soup.title)
    #return html.status_code
    ###################################### below is to test with webdriver
    #driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
    #driver = webdriver.Chrome()
    #driver.get('http://dell.com')



    return soup.title

start = time()

processes = []
with ThreadPoolExecutor(max_workers=13) as executor:
    for url in url_list:
        processes.append(executor.submit(download_file, url))
        print(psutil.cpu_percent(), " ****cpu")

for task in as_completed(processes):

    print(task.result())


    # gives a single float value
   # print(psutil.cpu_percent()," ****cpu")
    # gives an object with many fields
    print(psutil.virtual_memory())
    # you can convert that object to a dictionary
    dict(psutil.virtual_memory()._asdict())
    # you can have the percentage of used RAM
    print(psutil.virtual_memory().percent)
    # you can calculate percentage of available memory
    #print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)



print(f'Time taken: {time() - start}')