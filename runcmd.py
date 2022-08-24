import subprocess
from subprocess import Popen
import glob
import time
import psutil

start = time.time()
tests = glob.glob('xs*.py')
processes = []
for test in tests:
    processes.append(Popen('python %s' % test, shell=True))


for process in processes:
    process.wait()

print ("'%s\' fetched in %ss" % ("from main****** ", (time.time() - start)))
print("cpu percent", psutil.cpu_percent())