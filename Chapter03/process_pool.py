# Demonstrates parallel processing using a process pool

import multiprocessing


# Function executed by pool workers
def function_square(data):
    return data * data


if __name__ == '__main__':

    # Input data
    inputs = list(range(0, 100))

    # Create pool with 4 worker processes
    pool = multiprocessing.Pool(processes=4)

    # Apply function to all inputs
    pool_outputs = pool.map(function_square, inputs)

    pool.close()
    pool.join()

    print('Pool :', pool_outputs)