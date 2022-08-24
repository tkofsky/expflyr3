import threading
import sys
import selenium
from selenium import webdriver

driver=webdriver.Chrome("chromedriver.exe")
driver.get ("http://www.dell.com")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
text_file = open("flights.txt", "w",encoding="utf-8")  # out
driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')



from threading import  Thread
import time
start = time.perf_counter()




def do_something (seconds):
    print ('sleeping',seconds,'seconds')
    time.sleep(seconds)

    driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
    driver.get("http://www.dell.com")
    chk = driver.title
    print(chk)
    #print ('Done Sleeping...')


#do_something()
#t1= threading.Thread(target=do_something)
#t2= threading.Thread(target=do_something)
#t1.start()
#t2.start()
#t1.join()
#t2.join()

#finish=time.perf_counter()

#print (finish-start,"aaaaaa")

#exit ()


threads = []
for _ in range(10):
    t=threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)

#append a list of threads
for thread in threads:
    thread.join()


finish=time.perf_counter()

print (finish-start,"aaaaaa")

exit ()

import os
import math


def doit():
    for i in range(0,4000000):
        math.sqrt(i)

threads =[]



for i in range(4):
    print ('reg thread %d' %i)
    threads.append(Thread(target=doit))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join
