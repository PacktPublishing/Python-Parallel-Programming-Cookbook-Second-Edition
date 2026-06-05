# Queue in Multithreading

## Description
This code demonstrates thread synchronization using a Queue in Python.

## What This Code Does
- Creates one Producer and multiple Consumer threads  
- Producer generates random items and adds them to the queue  
- Consumers continuously remove items from the queue  
- Queue ensures safe communication between threads  

## Execution Flow
1. Create a Queue object  
2. Start Producer thread  
3. Start multiple Consumer threads  
4. Producer:
   - Generates random item  
   - Adds item to queue using `put()`  
   - Sleeps for 1 second  
5. Consumers:
   - Continuously fetch items using `get()`  
   - Process item  
   - Call `task_done()` after processing  
6. Threads run concurrently  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Producer-consumer problems  
- Thread-safe data sharing  
- Task scheduling systems  

## When to Use
Use when:
- Multiple threads need to share data safely  
- Task queue or pipeline is required  

Avoid when:
- No data sharing is needed  
- Simple synchronization is enough  

## How to Use
1. Import Queue from `queue` module  
2. Create queue using `Queue()`  
3. Use `put()` to add items  
4. Use `get()` to remove items  
5. Use `task_done()` after processing  

## Advantages
- Thread-safe by default  
- Easy to use  
- No need for manual locking  
- Efficient for producer-consumer pattern  

## Disadvantages
- Blocking behavior may delay threads  
- Less control compared to manual synchronization  
- Infinite loops can cause program to hang  

## One-Line Summary
Queue provides a thread-safe way to share data between producer and consumer threads.
