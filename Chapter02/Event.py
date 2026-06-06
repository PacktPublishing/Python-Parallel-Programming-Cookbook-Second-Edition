import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
# Event object for simple "stop/go" signaling between threads
event = threading.Event()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)
            # Blocks execution until event.set() is called by the producer
            event.wait()
            item = items.pop()
            logging.info('Consumer notify: {} popped by {}'\
                         .format(item, self.name))

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Producer notify: item {} appended by {}'\
                         .format(item, self.name))
            # Trigger the event and then immediately reset it
            event.set()
            event.clear()

if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
