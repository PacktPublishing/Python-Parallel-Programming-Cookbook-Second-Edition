import time
import os
from random import randint
from threading import Thread,currentThread


class Ferdy1184112 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      time.sleep(self.duration)
      out_list = list()
      self.do_something(randint(1,14), 1000000)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())

   def do_something(self, x, y):
    while y > 0:
      for x in range(15):
        h = 2**x
      y = y-1

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Ferdy1184112("Thread#1 ", 1,randint(1,10))
    thread2 = Ferdy1184112("Thread#2 ", 2,randint(1,10))
    thread3 = Ferdy1184112("Thread#3 ", 3,randint(1,10))
    thread4 = Ferdy1184112("Thread#4 ", 4,randint(1,10))
    thread5 = Ferdy1184112("Thread#5 ", 5,randint(1,10))
    thread6 = Ferdy1184112("Thread#6 ", 6,randint(1,10))
    thread7 = Ferdy1184112("Thread#7 ", 7,randint(1,10))
    thread8 = Ferdy1184112("Thread#8 ", 8,randint(1,10))
    thread9 = Ferdy1184112("Thread#9 ", 9,randint(1,10))

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


    


