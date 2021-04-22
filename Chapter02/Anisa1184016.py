import time
import os
from random import randint
from threading import Thread,currentThread


class AnisaRos1184016 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      self.pangkat(randint(2,19), 50)
      print (str(self.thread_number)+". ---> " + self.name + " over.")
      print (", Realname of Thread : " + currentThread().getName())

   def pangkat(self, x, y):
      while y>0:
        x=x**2
        y=y-1

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = AnisaRos1184016 ("Thread#1 ", 1,randint(1,10))
    thread2 = AnisaRos1184016 ("Thread#2 ", 2,randint(1,10))
    thread3 = AnisaRos1184016 ("Thread#3 ", 3,randint(1,10))
    thread4 = AnisaRos1184016 ("Thread#4 ", 4,randint(1,10))
    thread5 = AnisaRos1184016 ("Thread#5 ", 5,randint(1,10))
    thread6 = AnisaRos1184016 ("Thread#6 ", 6,randint(1,10))
    thread7 = AnisaRos1184016 ("Thread#7 ", 7,randint(1,10))
    thread8 = AnisaRos1184016 ("Thread#8 ", 8,randint(1,10))
    thread9 = AnisaRos1184016 ("Thread#9 ", 9,randint(1,10))

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


    


