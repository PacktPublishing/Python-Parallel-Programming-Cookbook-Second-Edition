# Demonstrates daemon (background) processes

import multiprocessing
import time


def foo():

    name = multiprocessing.current_process().name

    print("Starting %s\n" % name)

    if name == 'background_process':

        # Background process work
        for i in range(0, 5):
            print('---> %d\n' % i)

        time.sleep(1)

    else:

        # Normal process work
        for i in range(5, 10):
            print('---> %d\n' % i)

        time.sleep(1)

    print("Exiting %s\n" % name)


if __name__ == '__main__':

    # Daemon process
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )

    background_process.daemon = True

    # Non-daemon process
    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )

    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()