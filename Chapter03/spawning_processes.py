# Demonstrates basic process creation using multiprocessing

import multiprocessing


# Function executed by each process
def myFunc(i):
    print('calling myFunc from process n°: %s' % i)

    for j in range(0, i):
        print('output from myFunc is :%s' % j)

    return


if __name__ == '__main__':

    # Create and execute 6 processes
    for i in range(6):
        process = multiprocessing.Process(
            target=myFunc,
            args=(i,)
        )

        process.start()
        process.join()