import time
import os
from random import randint
from threading import Thread,currentThread


class Zanwar1184050 (Thread):
  def __init__(self, name,thread_number):
    Thread.__init__(self)
    self.name = name
    self.thread_number = thread_number
  def run(self):
    print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
    self.urut_angka("", randint(1,99), randint(1,99), 500000)
    print (str(self.thread_number)+". ---> " + self.name + " over.")
    print (", Realname of Thread : " + currentThread().getName())

  def urut_angka(self, string, x, y, i):
    string = ""
    while i>0:
      z = (x**2 + y**2)
      z = z ** 0.5
      string = string+str(z)
      i = i-1

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Zanwar1184050("Thread#1 ", 1)
    thread2 = Zanwar1184050("Thread#2 ", 2)
    thread3 = Zanwar1184050("Thread#3 ", 3)
    thread4 = Zanwar1184050("Thread#4 ", 4)
    thread5 = Zanwar1184050("Thread#5 ", 5)
    thread6 = Zanwar1184050("Thread#6 ", 6)
    thread7 = Zanwar1184050("Thread#7 ", 7)
    thread8 = Zanwar1184050("Thread#8 ", 8)
    thread9 = Zanwar1184050("Thread#9 ", 9)

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