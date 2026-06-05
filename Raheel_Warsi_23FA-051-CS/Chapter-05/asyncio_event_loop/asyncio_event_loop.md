# Asyncio Event Loop Task Scheduling

## Description
This code demonstrates task scheduling using the `asyncio` event loop in Python.

## What This Code Does
- Defines three tasks:
  - `task_A()`  
  - `task_B()`  
  - `task_C()`  
- Tasks call each other repeatedly  
- Uses `call_later()` for delayed scheduling  
- Runs tasks for 60 seconds using the event loop  

## Execution Flow
1. Create asyncio event loop  
2. Set loop end time (60 seconds)  
3. Start execution with `task_A()` using `call_soon()`  
4. Each task:
   - Prints task name  
   - Sleeps for random time  
   - Schedules next task using `call_later()`  
5. Loop continues until end time is reached  
6. Event loop stops and closes  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Task scheduling  
- Event-driven programming  
- Asynchronous workflows  
- Repeated background operations  

## When to Use
Use when:
- Tasks must run repeatedly  
- Delayed execution is required  
- Event loop scheduling is needed  

Avoid when:
- Simple sequential execution is enough  
- Heavy CPU processing is required  

## How to Use
1. Import `asyncio`  
2. Create tasks/functions  
3. Schedule tasks using:
   - `call_soon()`  
   - `call_later()`  
4. Run loop using `run_forever()`  
5. Stop loop using `loop.stop()`  

## Advantages
- Efficient task scheduling  
- Non-blocking execution model  
- Good for event-driven systems  

## Disadvantages
- Complex flow control  
- Harder debugging  
- `time.sleep()` blocks event loop  

## One-Line Summary
This program schedules and executes tasks repeatedly using the asyncio event loop.
