import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Semaphore starting at 0 forces the consumer to wait for producer's release
semaphore = threading.Semaphore(0)
item = 0


def consumer():
    logging.info('Consumer is waiting')
    # Decrements semaphore; blocks here because initial value is 0
    semaphore.acquire()
    logging.info('Consumer notify: item number {}'.format(item))


def producer():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Producer notify: item number {}'.format(item))
    # Decrements semaphore; blocks here because initial value is 0
    semaphore.release()


def main():
    for i in range(10):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
