# Semaphore in Multithreading

## Description
This code demonstrates the use of a Semaphore in Python threading.

## What This Code Does
- Creates producer and consumer threads  
- Consumer waits until resource is available  
- Producer generates a random item after delay  
- Producer releases semaphore to notify consumer  
- Consumer acquires semaphore and processes item  

## Execution Flow
1. Initialize semaphore with value 0  
2. Start consumer thread → waits using `acquire()`  
3. Start producer thread  
4. Producer:
   - Sleeps for 3 seconds  
   - Generates random item  
   - Prints item  
   - Calls `release()` on semaphore  
5. Consumer:
   - Unblocks after release  
   - Prints received item  
6. Repeat process 10 times  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Producer-consumer problems  
- Controlling access to shared resources  
- Synchronizing threads  

## When to Use
Use when:
- Limited resources need controlled access  
- Threads must wait for signal from other threads  

Avoid when:
- No shared resource management is needed  
- Tasks are independent  

## How to Use
1. Create semaphore using `threading.Semaphore()`  
2. Use `acquire()` to block thread  
3. Use `release()` to unblock waiting thread  
4. Implement logic in producer and consumer  

## Advantages
- Controls access to shared resources  
- Prevents race conditions  
- Useful for synchronization  

## Disadvantages
- Can cause deadlocks if misused  
- Hard to debug  
- Requires careful handling  

## One-Line Summary
Semaphore controls access to shared resources by allowing threads to wait and signal each other.
