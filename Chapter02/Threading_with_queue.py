""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random




class Producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        global adaantrian
        adaantrian = True
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify : item N°%d appended to queue by %s\n'\
                  % (item, self.name))
            time.sleep(1)
        self.queue.join()#akan memblokir sampai semua antrian beres
        print('selesai semua antrian')

class Consumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        

    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify : %d popped from queue by %s'\
                  % (item, self.name))
            
            self.queue.task_done()#penanda per antrian sudah di proses
            

if __name__ == '__main__':
    queue = Queue()
    adaantrian=False

    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    
#    t1.join()
#    t2.join()
#    t3.join()
#    t4.join()
