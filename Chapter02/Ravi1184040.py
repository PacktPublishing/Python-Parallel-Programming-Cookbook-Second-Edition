import time
import os
from random import randint
from threading import Thread,currentThread


class Ravi1184040 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      m=randint(1,15)
      n=randint(1,15)
      self.hore(m, n, 5000000)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())

   def hore(self, m, n, o):
       while o>0:
        m=m*n/2
        o=o-1

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Ravi1184040("Thread#1 ", 1,15)
    thread2 = Ravi1184040("Thread#2 ", 2,15)
    thread3 = Ravi1184040("Thread#3 ", 3,15)
    thread4 = Ravi1184040("Thread#4 ", 4,15)
    thread5 = Ravi1184040("Thread#5 ", 5,15)
    thread6 = Ravi1184040("Thread#6 ", 6,15)
    thread7 = Ravi1184040("Thread#7 ", 7,15)
    thread8 = Ravi1184040("Thread#8 ", 8,15)
    thread9 = Ravi1184040("Thread#9 ", 9,15)
    thread10 = Ravi1184040("Thread#10 ", 10,15)
    thread11 = Ravi1184040("Thread#11 ", 11,15)
    thread12 = Ravi1184040("Thread#12 ", 12,15)
    thread13 = Ravi1184040("Thread#13 ", 13,15)  
    thread14 = Ravi1184040("Thread#14 ", 14,15)                        
    thread15 = Ravi1184040("Thread#15 ", 15,15)                       
                           
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

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))
    return True


    


