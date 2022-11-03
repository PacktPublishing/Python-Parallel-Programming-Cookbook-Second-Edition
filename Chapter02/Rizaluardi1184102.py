import time
import os
from random import randint
from threading import Thread,currentThread


class Rizaluardi1184102 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      num=randint(3,12)
      nom=randint(3,12)
      self.rank(num, nom, 6600000)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())

   def rank(self, num, nom, hasil):
    while hasil>0:
        num=num*nom/3
        hasil=hasil-1

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Rizaluardi1184102("Thread#1 ", 1,12)
    thread2 = Rizaluardi1184102("Thread#2 ", 2,12)
    thread3 = Rizaluardi1184102("Thread#3 ", 3,12)
    thread4 = Rizaluardi1184102("Thread#4 ", 4,12)
    thread5 = Rizaluardi1184102("Thread#5 ", 5,12)
    thread6 = Rizaluardi1184102("Thread#6 ", 6,12)
    thread7 = Rizaluardi1184102("Thread#7 ", 7,12)
    thread8 = Rizaluardi1184102("Thread#8 ", 8,12)
    thread9 = Rizaluardi1184102("Thread#9 ", 9,12)

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


    


