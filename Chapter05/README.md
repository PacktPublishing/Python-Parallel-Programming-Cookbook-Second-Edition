**Chapter 05 — Asynchronous Programming**

This chapter covers asyncio — Python's way of handling many tasks concurrently without threads or processes. Instead of running tasks in parallel, asyncio switches between them whenever one is waiting (e.g., sleeping or doing I/O). Also covers concurrent.futures for a simpler pool-based approach.


**asyncio_event_loop.py — The Event Loop in Action**
Defines three tasks (A, B, C) that call each other in a chain using loop.call_later().
The loop runs for 60 seconds, cycling through the tasks and stopping when time runs out.


**asyncio_coroutine.py — Coroutines as a State Machine**
Models a Finite State Machine using coroutines — each state randomly transitions to another.
Uses yield from to hand control between states until the end_state is reached.


**asyncio_and_futures.py — Futures: Placeholder for a Result**
Two coroutines run concurrently — one counts a sum, the other computes a factorial.
Each stores its result in a Future object; a callback (got_result) prints it when done.


**asyncio_task_manipulation.py — Running Multiple Tasks Concurrently**
Creates three asyncio.Task objects for factorial, fibonacci, and binomial coefficient calculations.
All three run at the same time via the event loop — they take turns whenever asyncio.sleep(1) is hit.


**concurrent_futures_pooling.py — Thread Pool vs Process Pool**
Runs the same CPU task (counting to 10 million x N) three ways: sequential, thread pool, process pool.
Compares execution times — process pool wins for CPU-heavy work; thread pool is better for I/O tasks.


**Key Concepts**

Event Loop — The engine that runs and switches between async tasks
Coroutine — A function that can pause and resume with yield from / await
Future — A placeholder that holds a result once a task is done
Task — A coroutine wrapped and scheduled by the event loop
ThreadPoolExecutor — A pool of threads for concurrent I/O-bound work
ProcessPoolExecutor — A pool of processes for parallel CPU-bound work
