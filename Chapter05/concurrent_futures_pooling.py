# Compares sequential execution,
# thread pools, and process pools

import concurrent.futures
import time

# Input values
number_list = list(range(1, 11))


# CPU-intensive computation
def count(number):

    for i in range(0, 10000000):
        i += 1

    return i * number


# Execute computation for a given value
def evaluate(item):

    result_item = count(item)

    print(
        'Item %s, result %s'
        % (item, result_item)
    )


if __name__ == '__main__':

    # Sequential execution
    start_time = time.clock()

    for item in number_list:
        evaluate(item)

    print(
        'Sequential Execution in %s seconds'
        % (time.clock() - start_time)
    )

    # Thread pool execution
    start_time = time.clock()

    with concurrent.futures.ThreadPoolExecutor(
            max_workers=5) as executor:

        for item in number_list:
            executor.submit(evaluate, item)

    print(
        'Thread Pool Execution in %s seconds'
        % (time.clock() - start_time)
    )

    # Process pool execution
    start_time = time.clock()

    with concurrent.futures.ProcessPoolExecutor(
            max_workers=5) as executor:

        for item in number_list:
            executor.submit(evaluate, item)

    print(
        'Process Pool Execution in %s seconds'
        % (time.clock() - start_time)
    )