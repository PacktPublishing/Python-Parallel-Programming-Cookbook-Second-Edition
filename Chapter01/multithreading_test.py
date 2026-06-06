from do_something import *
import time
import threading

# Multithreading benchmark
if __name__ == "__main__":
    start_time = time.time()

    size = 10000000
    threads = 10
    jobs = []

    # Create threads
    for i in range(threads):
        out_list = []
        thread = threading.Thread(
            target=do_something,
            args=(size, out_list)
        )
        jobs.append(thread)

    # Start all threads
    for j in jobs:
        j.start()

    # Wait for all threads to finish
    for j in jobs:
        j.join()

    print("List processing complete")

    end_time = time.time()
    print("multithreading time =", end_time - start_time)