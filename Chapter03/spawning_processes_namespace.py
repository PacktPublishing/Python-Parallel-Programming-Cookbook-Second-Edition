# Demonstrates process creation using an imported function

import multiprocessing
from myFunc import myFunc


if __name__ == '__main__':

    # Create processes using external function definition
    for i in range(6):
        process = multiprocessing.Process(
            target=myFunc,
            args=(i,)
        )

        process.start()
        process.join()