"""Asyncio using Asyncio.Task to execute three math functions in parallel"""

import asyncio


@asyncio.coroutine
def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Asyncio.Task: Compute factorial(%s)' % i)
        yield from asyncio.sleep(1)
        fact *= i
    print('Asyncio.Task - factorial(%s) = %s' % (number, fact))


@asyncio.coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print('Asyncio.Task: Compute fibonacci(%s)' % i)
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print('Asyncio.Task - fibonacci(%s) = %s' % (number, a))


@asyncio.coroutine
def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
        print('Asyncio.Task: Compute binomial_coefficient(%s)' % i)
        yield from asyncio.sleep(1)
    print('Asyncio.Task - binomial_coefficient(%s, %s) = %s' % (n, k, result))


if __name__ == '__main__':
    task_list = [asyncio.Task(factorial(10)),
                 asyncio.Task(fibonacci(10)),
                 asyncio.Task(binomial_coefficient(20, 10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()
