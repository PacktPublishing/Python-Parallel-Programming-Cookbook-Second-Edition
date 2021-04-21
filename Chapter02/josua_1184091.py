# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 16:56:22 2021

@author: Josuansef Pardede (1184091)
"""

import time
import os
from random import randint
from threading import Thread,currentThread


class josua_1184091 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      d=randint(1,20)
      e=randint(1,20)
      self.josh(d, e, 3000000)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())

   def josh(self, d, e, f):
       while f>0:
        d=d*e/40
        f=f-2


def main():
    start_time = time.time()
    
    # Thread Creation
    #thread1 = MyThreadClass("Thread#1 ", randint(1,10))
    thread1 = josua_1184091("Thread#1 ", 1,20)
    thread2 = josua_1184091("Thread#2 ", 2,20)
    thread3 = josua_1184091("Thread#3 ", 3,20)
    thread4 = josua_1184091("Thread#4 ", 4,20)
    thread5 = josua_1184091("Thread#5 ", 5,20)
    thread6 = josua_1184091("Thread#6 ", 6,20)
    thread7 = josua_1184091("Thread#7 ", 7,20)
    thread8 = josua_1184091("Thread#8 ", 8,20)
    thread9 = josua_1184091("Thread#9 ", 9,20)
    thread10 = josua_1184091("Thread#10 ", 10,20)
    thread11 = josua_1184091("Thread#11 ", 11,20)
    thread12 = josua_1184091("Thread#12 ", 12,20)
    thread13 = josua_1184091("Thread#13", 13,20)
    thread14 = josua_1184091("Thread#14", 14,20)
    thread15 = josua_1184091("Thread#15", 15,20)
    thread16 = josua_1184091("Thread#16", 16,20)
    thread17 = josua_1184091("Thread#17", 17,20)
    thread18 = josua_1184091("Thread#18", 18,20)
    thread19 = josua_1184091("Thread#19", 19,20)
    thread20 = josua_1184091("Thread#20", 20,20)
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
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()
    thread17.start()
    thread18.start()
    thread19.start()
    thread20.start()

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
    thread10.join()
    thread11.join()
    thread12.join()
    thread13.join()
    thread14.join()
    thread15.join()
    thread16.join()
    thread17.join()
    thread18.join()
    thread19.join()
    thread20.join()

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))
    return True

    


