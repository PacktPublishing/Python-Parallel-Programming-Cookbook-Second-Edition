import os
import time
import threading
import multiprocessing
import random
 
NUM_WORKERS = 10
size = 10000000
out_list = list()

def do_something(count, out_list):
	for i in range(count):
		out_list.append(random.random())
"""
#Serial
start_time = time.time()
for _ in range(NUM_WORKERS):
    do_something(size,out_list)
end_time = time.time()
print("Serial time=", end_time - start_time)
"""

#MultiThreading
start_time = time.time()
jobs = []
for i in range(0, NUM_WORKERS):
    thread = threading.Thread(target=do_something(size, out_list))
    jobs.append(thread)
for j in jobs:
    j.start()
    
for j in jobs:
    j.join()

print ("List processing complete.")
end_time = time.time()
print("threading time=", end_time - start_time)


#MultiProcesses
start_time = time.time()
jobs = []
for i in range(0, NUM_WORKERS):
    process = multiprocessing.Process\
              (target=do_something,args=(size,out_list))
    jobs.append(process)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

print ("List processing complete.")
end_time = time.time()
print("processes time=", end_time - start_time)
