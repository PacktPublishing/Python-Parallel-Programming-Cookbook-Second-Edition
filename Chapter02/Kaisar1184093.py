import time
import os
from random import randint
from threading import Thread,currentThread


class Kaisar1184093 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      x=randint(1,9)
      y=randint(1,9)
      self.pangkat(x, y, 1500000)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())

   def pangkat(self, x, y, z):
    while z>0:
        x=x*y/2
        z=z-1

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Kaisar1184093("Thread#1 ", 1,15)
    thread2 = Kaisar1184093("Thread#2 ", 2,15)
    thread3 = Kaisar1184093("Thread#3 ", 3,15)
    thread4 = Kaisar1184093("Thread#4 ", 4,15)
    thread5 = Kaisar1184093("Thread#5 ", 5,15)
    thread6 = Kaisar1184093("Thread#6 ", 6,15)
    thread7 = Kaisar1184093("Thread#7 ", 7,15)
    thread8 = Kaisar1184093("Thread#8 ", 8,15)
    thread9 = Kaisar1184093("Thread#9 ", 9,15)

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


    


