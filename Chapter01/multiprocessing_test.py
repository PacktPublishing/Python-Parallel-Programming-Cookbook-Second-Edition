from do_something import *
import time
import multiprocessing

# Multiprocessing benchmark
if __name__ == "__main__":
    start_time = time.time()

    size = 10000000
    procs = 10
    jobs = []

    # Create processes
    for i in range(procs):
        out_list = []

        process = multiprocessing.Process(
            target=do_something,
            args=(size, out_list)
        )

        jobs.append(process)

    # Start all processes
    for j in jobs:
        j.start()

    # Wait for all processes to finish
    for j in jobs:
        j.join()

    print("List processing complete")

    end_time = time.time()
    print("multiprocesses time =", end_time - start_time)