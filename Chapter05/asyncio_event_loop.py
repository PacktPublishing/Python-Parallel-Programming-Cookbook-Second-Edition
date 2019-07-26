import asyncio
import time
import random

def task_A(end_time, loop):
    print ("task_A called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_B, end_time, loop)
    else:
        loop.stop()

def task_B(end_time, loop):
    print ("task_B called ")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_C, end_time, loop)
    else:
        loop.stop()

def task_C(end_time, loop):
    print ("task_C called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_A, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 60
loop.call_soon(task_A, end_loop, loop)
loop.run_forever()
loop.close()

