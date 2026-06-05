import asyncio
import sys


@asyncio.coroutine
def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    yield from asyncio.sleep(4)
    future.set_result('First coroutine (sum of N ints) result = %s' % count)


@asyncio.coroutine
def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    yield from asyncio.sleep(4)
    future.set_result('Second coroutine (factorial) result = %s' % count)


def got_result(future):
    print(future.result())

if __name__ == '__main__':
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    tasks = [first_coroutine(future1, num1),
             second_coroutine(future2, num2)]

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
