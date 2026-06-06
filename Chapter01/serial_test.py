import time
from do_something import *

# Serial execution benchmark
if __name__ == "__main__":
    start_time = time.time()

    size = 10000000
    n_exec = 10

    # Execute workload sequentially
    for i in range(n_exec):
        out_list = []
        do_something(size, out_list)

    print("List processing complete.")

    end_time = time.time()
    print("serial time =", end_time - start_time)
