# Demonstrates process termination

import multiprocessing
import time


def foo():

    print('Starting function')

    for i in range(0, 10):
        print('-->%d\n' % i)
        time.sleep(1)

    print('Finished function')


if __name__ == '__main__':

    # Create process
    p = multiprocessing.Process(target=foo)

    print('Process before execution:', p, p.is_alive())

    # Start process
    p.start()

    print('Process running:', p, p.is_alive())

    # Forcefully terminate process
    p.terminate()

    print('Process terminated:', p, p.is_alive())

    # Wait for cleanup
    p.join()

    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)