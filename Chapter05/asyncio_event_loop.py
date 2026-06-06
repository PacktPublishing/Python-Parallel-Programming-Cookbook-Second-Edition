# Demonstrates scheduling tasks using an asyncio event loop

import asyncio
import time
import random


# First scheduled task
def task_A(end_time, loop):

    print("task_A called")

    time.sleep(random.randint(0, 5))

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_B, end_time, loop)
    else:
        loop.stop()


# Second scheduled task
def task_B(end_time, loop):

    print("task_B called")

    time.sleep(random.randint(0, 5))

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_C, end_time, loop)
    else:
        loop.stop()


# Third scheduled task
def task_C(end_time, loop):

    print("task_C called")

    time.sleep(random.randint(0, 5))

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_A, end_time, loop)
    else:
        loop.stop()


# Create event loop
loop = asyncio.get_event_loop()

# Set execution duration
end_loop = loop.time() + 60

# Schedule first task
loop.call_soon(task_A, end_loop, loop)

# Start event loop
loop.run_forever()

# Close loop after completion
loop.close()