import time
from Chapter01.do_something import *



def serial_test():
    start_time = time.time()
    size = 10000000   
    n_exec = 10
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
