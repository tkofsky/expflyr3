import psutil
import threading
import requests
import time
from bs4 import BeautifulSoup
import os
from selenium import webdriver

start = time.time()
urls = ["http://www.microsoft.com","http://www.google.com", "http://www.apple.com",  "http://www.amazon.com", "http://www.facebook.com"]

text_file = open("threaddata.txt", "w") #

for url in urls:
    #page = requests.get(url)
    #print(page.text)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    print(soup.title)
    print("'%s\' fetched in %ss" % (url, (time.time() - start)))
    print("cpu percent", psutil.cpu_percent())



print ("***Elapsed Time: %s" % (time.time() - start))
text_file.write("non thread time "+str(time.time()-start)+'\n')



start = time.time()
urls = ["http://www.microsoft.com","http://www.google.com", "http://www.apple.com",  "http://www.amazon.com", "http://www.facebook.com"]

def fetch_url(url):
    #urlHandler = urllib2.urlopen(url)
    #html = urlHandler.read()

    r=requests.get(url)


    soup = BeautifulSoup(r.text)
    #driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')

    #driver.get("http://www.dell.com")
    #soup = BeautifulSoup(driver.page_source)

    print (soup.title)
    print ("'%s\' fetched in %ss" % (url, (time.time() - start)))

    text_file.write("thread time "+str(time.time() - start)+"\n")
    # gives a single float value
    print ("thread cpu percent",str(psutil.cpu_percent()))
    #text_file.write(psutil.cpu_percent())
    #text_file.write("thread cpu percent "+aa+"\n")

    # gives an object with many fields
    #psutil.virtual_memory()
    # you can convert that object to a dictionary
    #dict(psutil.virtual_memory()._asdict())
    # you can have the percentage of used RAM
    #psutil.virtual_memory().percent

    # you can calculate percentage of available memory
 #psutil.virtual_memory().available * 100 / psutil.virtual_memory().total




threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print ("***Elapsed Time: %s" % (time.time() - start))
text_file.write("total thread "+str(time.time() - start)+"\n")

#
text_file.flush()
os.fsync(text_file.fileno())
text_file.close()