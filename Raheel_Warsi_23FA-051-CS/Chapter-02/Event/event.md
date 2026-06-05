# Event in Multithreading

## Description
This code demonstrates the use of an Event in Python threading. 

## What This Code Does
- Creates Producer and Consumer threads  
- Producer generates items and adds them to a list  
- Producer signals the event after adding item  
- Consumer waits for event signal  
- Consumer removes item from list after signal  

## Execution Flow
1. Initialize shared list (`items`)  
2. Create an Event object  
3. Start Producer and Consumer threads  
4. Producer:
   - Sleeps for 2 seconds  
   - Generates random item  
   - Appends item to list  
   - Calls `event.set()` to signal  
   - Calls `event.clear()` to reset  
5. Consumer:
   - Waits using `event.wait()`  
   - Pops item from list  
   - Prints consumed item  
6. Process continues until Producer finishes  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Thread communication  
- Signaling between threads  
- Producer-consumer coordination  

## When to Use
Use when:
- One thread needs to notify others  
- Tasks depend on a signal/event  

Avoid when:
- No synchronization is required  
- Threads are independent  

## How to Use
1. Create event using `threading.Event()`  
2. Use `event.wait()` to block thread  
3. Use `event.set()` to signal  
4. Use `event.clear()` to reset event  

## Advantages
- Simple signaling mechanism  
- Easy communication between threads  
- Useful for coordination  

## Disadvantages
- Can miss signals if not handled properly  
- Requires careful timing  
- Not suitable for complex synchronization  

## One-Line Summary
Event allows one thread to signal others to start or continue execution.
