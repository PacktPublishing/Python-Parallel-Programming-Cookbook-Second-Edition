**Chapter 02 — Thread-Based Parallelism**

This chapter covers Python's threading module — how to create threads, manage them, and keep them from stepping on each other's toes using synchronization tools.


**Thread_definition.py — Creating Your First Threads**
Creates 10 threads, each calling my_func with its thread number.
Threads are started and immediately joined (waited for) one by one.


**Thread_determine.py — Named Threads Running Together**
Creates 3 named threads (function_A, B, C), each sleeping for 2 seconds.
All three are started together, then waited on — shows threads running concurrently.


**Thread_name_and_processes.py — Thread Class with Custom Name**
Defines a custom MyThreadClass by extending Python's Thread class.
Each thread prints its name and the process ID it belongs to when it runs.


**MyThreadClass.py — Threads with Random Durations**
Spawns 9 threads, each sleeping for a random time (1–10 seconds).
Shows that threads finish in unpredictable order depending on their sleep duration.


**MyThreadClass_lock.py — Lock: One Thread at a Time**
Same as MyThreadClass.py but adds a Lock — only one thread can run its body at a time.
The lock is acquired at the start of run() and released at the end, making threads execute one after another.


**MyThreadClass_lock_2.py — Lock: Only Protect What Matters**
Similar to lock.py but the lock is released before the sleep — only the print is locked, not the wait.
Threads can now overlap during their sleep, making it faster while still protecting shared output.


**Rlock.py — Reentrant Lock (RLock)**
A Box class uses an RLock so the same thread can acquire the lock multiple times without deadlocking.
Two threads (adder and remover) modify a shared counter safely using add() and remove().


**Semaphore.py — Semaphore: Signal Between Threads**
Producer generates a random number and calls semaphore.release() to signal it's ready.
Consumer waits on semaphore.acquire() — it won't proceed until the producer signals it.


**Event.py — Event: One Thread Signals Another**
Producer adds a random item to a list and calls event.set() to notify the consumer.
Consumer waits on event.wait() and processes the item once the event is triggered.


**Condition.py — Condition: Producer-Consumer with State Check**
Producer adds items to a shared list (max 10) and notifies the consumer via a Condition.
Consumer waits if the list is empty, then pops an item and notifies the producer to continue.


**Threading_with_queue.py — Queue: Safest Way to Share Data**
1 Producer puts 5 random items into a Queue; 3 Consumers pull from it concurrently.
Queue handles all the synchronization internally — no manual locks needed.


**Synchronization Tools at a Glance**

Lock — Only one thread runs a section at a time
RLock — Like Lock, but the same thread can re-acquire it
Semaphore — Controls how many threads can access something at once
Event — One thread signals others to proceed
Condition — Threads wait/notify based on a shared condition
Queue — Thread-safe data sharing — the simplest option
