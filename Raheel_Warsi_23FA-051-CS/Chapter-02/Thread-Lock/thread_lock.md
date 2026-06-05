# Lock in Multithreading

## Description
This code demonstrates the use of a Lock in Python threading. 

## What This Code Does
- Creates multiple threads (9 threads)  
- Each thread runs for a random duration  
- Uses a Lock to allow only one thread to execute at a time  
- Ensures synchronized execution of threads  

## Execution Flow
1. Create a global Lock (`threadLock`)  
2. Define a thread class (`MyThreadClass`)  
3. Each thread:
   - Acquires lock using `acquire()`  
   - Prints start message  
   - Sleeps for random time  
   - Prints end message  
   - Releases lock using `release()`  
4. Start all threads  
5. Wait for all threads using `join()`  
6. Print total execution time  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Preventing race conditions  
- Controlling access to shared resources  
- Ensuring one thread runs at a time  

## When to Use
Use when:
- Multiple threads access shared data  
- Only one thread should execute critical section  

Avoid when:
- Threads are independent  
- No shared resource conflict exists  

## How to Use
1. Create lock using `threading.Lock()`  
2. Use `lock.acquire()` before critical section  
3. Use `lock.release()` after execution  
4. Alternatively use `with lock:` for cleaner code  

## Advantages
- Simple and easy to use  
- Prevents data corruption  
- Ensures thread safety  

## Disadvantages
- Reduces parallelism (one thread at a time)  
- Can cause deadlocks if not handled properly  
- Slows down execution  

## One-Line Summary
Lock allows only one thread to access a resource at a time to ensure safe execution.
