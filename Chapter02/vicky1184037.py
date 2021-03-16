import time
import os
from random import randint
from threading import Thread,currentThread


class vicky1184037 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      time.sleep(self.duration)
      out_list = list()
      self.do_something(1000000,out_list)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())

import time
from do_something import

if __name__ == "__main__" :
	start_time = time.time()
	size = 10000000
	n_exec = 10
	for i in range(0, n_exec) :
		out_list = list()
		do_something(size, out_list)
	
	print ("List processing complate.")
	end_time = time.time()
	print("serial time-", end_time - start_time)



def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = vicky1184037("Thread#1 ", 1,randint(1,10))
    thread2 = vicky1184037("Thread#2 ", 2,randint(1,10))
    thread3 = vicky1184037("Thread#3 ", 3,randint(1,10))
    thread4 = vicky1184037("Thread#4 ", 4,randint(1,10))
    thread5 = vicky1184037("Thread#5 ", 5,randint(1,10))
    thread6 = vicky1184037("Thread#6 ", 6,randint(1,10))
    thread7 = vicky1184037("Thread#7 ", 7,randint(1,10))
    thread8 = vicky1184037("Thread#8 ", 8,randint(1,10))
    thread9 = vicky1184037("Thread#9 ", 9,randint(1,10))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))
    return True


    


