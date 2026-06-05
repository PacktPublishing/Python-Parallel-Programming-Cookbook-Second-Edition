# Queue in Multiprocessing

## Description
This code demonstrates the use of a Queue in Python multiprocessing.

## What This Code Does
- Creates a Producer process and a Consumer process  
- Producer generates random items and adds them to the queue  
- Consumer removes items from the queue  
- Displays queue size and processed items  

## Execution Flow
1. Create a multiprocessing Queue  
2. Start Producer process  
3. Start Consumer process  
4. Producer:
   - Generates random item  
   - Adds item using `put()`  
   - Prints queue size  
5. Consumer:
   - Checks if queue is empty  
   - Retrieves item using `get()`  
   - Prints consumed item  
6. Both processes run concurrently  
7. Main process waits using `join()`  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Inter-process communication (IPC)  
- Producer-consumer systems  
- Data sharing between processes  

## When to Use
Use when:
- Multiple processes need to share data  
- Safe communication between processes is required  

Avoid when:
- No data sharing is needed  
- Simple tasks without communication  

## How to Use
1. Create queue using `multiprocessing.Queue()`  
2. Use `put()` to add items  
3. Use `get()` to retrieve items  
4. Use `empty()` and `qsize()` for status  

## Advantages
- Process-safe data sharing  
- Easy to use  
- Handles synchronization internally  

## Disadvantages
- Slower than threading queue  
- Overhead due to inter-process communication  
- `qsize()` may not always be accurate on all systems  

## One-Line Summary
Multiprocessing Queue allows safe data sharing between processes using a producer-consumer model.
