import time
import os
from random import randint
from threading import Thread,currentThread


class IrfanHernandez1184014 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      time.sleep(self.duration)
      out_list = [2,54,38,76,23,56,84,90]
      self.do_something(out_list)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())

   def do_something(self,out_list):
    for j in range(len(out_list)-1,-1,-1):
        hole = j
        while hole <(len(out_list)-1) and out_list[hole+1]>out_list[hole]:
            out_list[hole] = out_list[hole+1]
            hole = hole+1
            out_list[hole] = out_list[j]
        out_list = list()

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = IrfanHernandez1184014("Thread#1 ", 1,randint(1,10))
    thread2 = IrfanHernandez1184014("Thread#2 ", 2,randint(1,10))
    thread3 = IrfanHernandez1184014("Thread#3 ", 3,randint(1,10))
    thread4 = IrfanHernandez1184014("Thread#4 ", 4,randint(1,10))
    thread5 = IrfanHernandez1184014("Thread#5 ", 5,randint(1,10))
    thread6 = IrfanHernandez1184014("Thread#6 ", 6,randint(1,10))
    thread7 = IrfanHernandez1184014("Thread#7 ", 7,randint(1,10))
    thread8 = IrfanHernandez1184014("Thread#8 ", 8,randint(1,10))
    thread9 = IrfanHernandez1184014("Thread#9 ", 9,randint(1,10))

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


    


