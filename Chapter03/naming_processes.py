# Demonstrates assigning names to processes

import multiprocessing
import time


def myFunc():

    # Get current process name
    name = multiprocessing.current_process().name

    print("Starting process name = %s\n" % name)

    time.sleep(3)

    print("Exiting process name = %s\n" % name)


if __name__ == '__main__':

    # Process with custom name
    process_with_name = multiprocessing.Process(
        name='myFunc process',
        target=myFunc
    )

    # Process with default system-generated name
    process_with_default_name = multiprocessing.Process(
        target=myFunc
    )

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()