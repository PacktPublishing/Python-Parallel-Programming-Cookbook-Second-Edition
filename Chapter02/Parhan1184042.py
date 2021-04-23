import time
import os
import random
from random import randint
from threading import Thread,currentThread


class Parhan1184042 (Thread):
   def __init__(self, name,thread_number, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
      self.thread_number = thread_number
   def run(self):
      print ("\n"+str(self.thread_number)+". ---> " + self.name + " running, belonging to process ID "+ str(os.getpid()) + "\n")
      color_number={'red','yellow','blue','green','black','pink','orange','jingga','Abu abu','blue black','coklat'}
      self.get_color(1000000)
      print (str(self.thread_number)+". ---> " + self.name + " over, sleep duration : " +str(self.duration) +" second")
      print (", Realname of Thread : " + currentThread().getName())
      
      def get_color(color_number=10):
        color_number = int(color_number)
        def do_something(color_number):
            student_array = []
            for i in range(1000000):
                random_color_number = random.randint(0, 4)
                color = get_color(random_color_number)
                student_array.append(color)
       
def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Parhan1184042("Thread#1 ", 1,randint(1,10))
    thread2 = Parhan1184042("Thread#2 ", 2,randint(1,10))
    thread3 = Parhan1184042("Thread#3 ", 3,randint(1,10))
    thread4 = Parhan1184042("Thread#4 ", 4,randint(1,10))
    thread5 = Parhan1184042("Thread#5 ", 5,randint(1,10))
    thread6 = Parhan1184042("Thread#6 ", 6,randint(1,10))
    thread7 = Parhan1184042("Thread#7 ", 7,randint(1,10))
    thread8 = Parhan1184042("Thread#8 ", 8,randint(1,10))
    thread9 = Parhan1184042("Thread#9 ", 9,randint(1,10))

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


    


