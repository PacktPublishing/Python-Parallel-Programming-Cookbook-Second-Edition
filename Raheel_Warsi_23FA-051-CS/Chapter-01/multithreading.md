# Multithreading Example

## Description
This code demonstrates how to use multithreading in Python to run tasks concurrently. 

## What This Code Does
- Runs a function `do_something` using 10 threads  
- Each thread handles a task (`size = 10,000,000`)  
- Measures total execution time  

## Execution Flow
1. Create 10 threads  
2. `start()` → runs all threads  
3. `join()` → waits until all threads finish  
4. Prints total execution time  

## End Use
Used for tasks such as:
- I/O operations (file handling, network requests)  
- Background tasks  
- Lightweight concurrent operations  

## When to Use
Use when:
- Task is I/O-bound  
- Multiple tasks can run concurrently  

Avoid when:
- Task is CPU-intensive (use multiprocessing instead)  

## How to Use
1. Define the function (`do_something`)  
2. Create threads using `threading.Thread`  
3. Start threads using `start()`  
4. Wait for completion using `join()`  

## Advantages
- Lightweight and faster to create than processes  
- Shared memory between threads  
- Suitable for I/O-bound tasks  

## Disadvantages
- Limited performance for CPU tasks (due to GIL)  
- Can cause race conditions  
- Debugging can be difficult  

## One-Line Summary
Multithreading runs multiple threads concurrently, best suited for I/O-bound tasks.
