import time
import os
from random import randint
from threading import Thread

# Custom thread implementation
class MyThreadClass(Thread):

    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print("---> " + self.name +
              " running, belonging to process ID "
              + str(os.getpid()))

        time.sleep(self.duration)

        print("---> " + self.name + " over")


def main():

    start_time = time.time()

    # Create multiple threads
    threads = [
        MyThreadClass(f"Thread#{i}", randint(1, 10))
        for i in range(1, 10)
    ]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for completion
    for thread in threads:
        thread.join()

    print("End")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()