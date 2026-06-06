import threading
import time
import os
from threading import Thread
from random import randint

# Lock for mutual exclusion
threadLock = threading.Lock()


class MyThreadClass(Thread):

    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):

        # Only one thread can enter this section at a time
        threadLock.acquire()

        print("---> " + self.name +
              " running, belonging to process ID "
              + str(os.getpid()))

        time.sleep(self.duration)

        print("---> " + self.name + " over")

        threadLock.release()


def main():

    start_time = time.time()

    threads = [
        MyThreadClass(f"Thread#{i}", randint(1, 10))
        for i in range(1, 10)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("End")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()