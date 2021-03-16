# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:01:27 2021

@author: HP
"""

import time
import os
from random import randint
from threading import Thread,currentThread


class baharandili1184002 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      a = 1
      b = 4
      n = 0
      self.aritmatika(a,b,n)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())
      

   def aritmatika(self, a, b, n):
       for n in range (2500000):
           n = n + 1
           a = a + b
   
def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = baharandili1184002("Thread#1 ", 1,randint(1,10))
    thread2 = baharandili1184002("Thread#2 ", 2,randint(1,10))
    thread3 = baharandili1184002("Thread#3 ", 3,randint(1,10))
    thread4 = baharandili1184002("Thread#4 ", 4,randint(1,10))
    thread5 = baharandili1184002("Thread#5 ", 5,randint(1,10))
    thread6 = baharandili1184002("Thread#6 ", 6,randint(1,10))
    thread7 = baharandili1184002("Thread#7 ", 7,randint(1,10))
    thread8 = baharandili1184002("Thread#8 ", 8,randint(1,10))
    thread9 = baharandili1184002("Thread#9 ", 9,randint(1,10))

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


    


