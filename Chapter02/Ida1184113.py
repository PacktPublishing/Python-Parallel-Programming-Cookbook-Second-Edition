import time
import os
from random import randint
from threading import Thread,currentThread


class Ida1184113 (Thread):
  def __init__(self, name,thread_number):
    Thread.__init__(self)
    self.name = name
    self.thread_number = thread_number
  def run(self):
    print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
    self.do_something(randint(200, 999), 170000)
    print (str(self.thread_number)+". ---> " + self.name + " over.")
    print (", Realname of Thread : " + currentThread().getName())

  def do_something(self, n, x):
    while x > 0:
        n = n*3
        x = x-1

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Ida1184113("Thread#1 ", 1)
    thread2 = Ida1184113("Thread#2 ", 2)
    thread3 = Ida1184113("Thread#3 ", 3)
    thread4 = Ida1184113("Thread#4 ", 4)
    thread5 = Ida1184113("Thread#5 ", 5)
    thread6 = Ida1184113("Thread#6 ", 6)
    thread7 = Ida1184113("Thread#7 ", 7)
    thread8 = Ida1184113("Thread#8 ", 8)
    thread9 = Ida1184113("Thread#9 ", 9)

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


    


