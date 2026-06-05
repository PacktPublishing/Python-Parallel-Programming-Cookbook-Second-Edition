# Condition in Multithreading

## Description
This code demonstrates the use of a Condition in Python threading.

## What This Code Does
- Creates Producer and Consumer threads  
- Producer adds items to a shared list  
- Consumer removes items from the list  
- Producer waits if list reaches limit (10 items)  
- Consumer waits if list is empty  
- Threads notify each other to continue execution  

## Execution Flow
1. Initialize shared list (`items`)  
2. Create a Condition object  
3. Start Producer and Consumer threads  
4. Producer:
   - Sleeps for 0.5 seconds  
   - Checks if list size is 10 → waits  
   - Adds item to list  
   - Calls `notify()`  
5. Consumer:
   - Sleeps for 2 seconds  
   - Checks if list is empty → waits  
   - Removes item from list  
   - Calls `notify()`  
6. Both threads coordinate using condition  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Producer-consumer problems  
- Thread coordination with conditions  
- Managing shared resources  

## When to Use
Use when:
- Threads depend on certain conditions  
- Need both waiting and notification mechanism  

Avoid when:
- Simple synchronization is enough (use Lock or Event)  
- No shared resource control is required  

## How to Use
1. Create condition using `threading.Condition()`  
2. Use `with condition:` for locking  
3. Use `condition.wait()` to block  
4. Use `condition.notify()` to wake up threads  

## Advantages
- Advanced synchronization mechanism  
- Efficient for producer-consumer problems  
- Allows fine control over thread execution  

## Disadvantages
- More complex than other methods  
- Risk of deadlocks if misused  
- Hard to debug  

## One-Line Summary
Condition allows threads to wait and notify each other based on specific conditions.
