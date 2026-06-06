# Demonstrates asyncio Futures and callback handling

import asyncio
import sys


# Counts numbers asynchronously
@asyncio.coroutine
def first_coroutine(future, num):

    count = 0

    for i in range(1, num + 1):
        count += 1

    yield from asyncio.sleep(4)

    future.set_result(
        'First coroutine '
        '(sum of N ints) result = %s'
        % count
    )


# Computes factorial asynchronously
@asyncio.coroutine
def second_coroutine(future, num):

    count = 1

    for i in range(2, num + 1):
        count *= i

    yield from asyncio.sleep(4)

    future.set_result(
        'Second coroutine '
        '(factorial) result = %s'
        % count
    )


# Callback executed when Future completes
def got_result(future):

    print(future.result())


if __name__ == '__main__':

    # Read command-line arguments
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Create event loop
    loop = asyncio.get_event_loop()

    # Create Future objects
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Create coroutine tasks
    tasks = [
        first_coroutine(future1, num1),
        second_coroutine(future2, num2)
    ]

    # Register callbacks
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # Execute coroutines
    loop.run_until_complete(
        asyncio.wait(tasks)
    )

    loop.close()