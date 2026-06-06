""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random

# The Producer adds data to a thread-safe Queue
class Producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            # .put() handles all internal locking automatically
            self.queue.put(item)
            print('Producer notify : item N°%d appended to queue by %s\n'\
                  % (item, self.name))
            time.sleep(1)

# Consumers retrieve data from the same Queue concurrently
class Consumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # .get() will block if the queue is empty until an item is available
            item = self.queue.get()
            print('Consumer notify : %d popped from queue by %s'\
                  % (item, self.name))
            # Signals that the specific item has been processed
            self.queue.task_done()

if __name__ == '__main__':
    # A Queue object is inherently thread-safe for many-to-many communication
    queue = Queue()

    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    # Note: Consumer threads in this script will run indefinitely   
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # The consumer joins would block indefinitely here as they are in 'while True' loops
    t1.join()
    t2.join()
    t3.join()
    t4.join()
