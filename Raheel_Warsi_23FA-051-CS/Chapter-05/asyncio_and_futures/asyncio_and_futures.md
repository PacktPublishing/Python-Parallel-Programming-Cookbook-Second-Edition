# Asyncio Coroutines in Python

## Description
This code demonstrates asynchronous programming using `asyncio` coroutines to execute multiple tasks concurrently.

## What This Code Does
- Defines two coroutines:
  - First coroutine calculates sum count  
  - Second coroutine calculates factorial  
- Uses `Future` objects to store results  
- Executes both coroutines concurrently  
- Prints results using callback functions  

## Execution Flow
1. Read two numbers from command-line arguments  
2. Create asyncio event loop  
3. Create two `Future` objects  
4. Create coroutine tasks:
   - `first_coroutine()`  
   - `second_coroutine()`  
5. Add callback functions using `add_done_callback()`  
6. Run tasks concurrently using `asyncio.wait()`  
7. Print results after completion  
8. Close event loop  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py 5 6
   ```

## End Use
Used for:
- Asynchronous task execution  
- Concurrent I/O operations  
- Non-blocking programming  

## When to Use
Use when:
- Multiple tasks can run concurrently  
- Waiting operations (I/O, APIs, timers) are involved  

Avoid when:
- Heavy CPU computation is required  
- Simple sequential execution is enough  

## How to Use
1. Import `asyncio`  
2. Define coroutines using `@asyncio.coroutine`  
3. Use `yield from` for async waiting  
4. Create tasks and futures  
5. Run tasks using event loop  

## Advantages
- Efficient concurrent execution  
- Non-blocking operations  
- Lightweight compared to threads/processes  

## Disadvantages
- Complex for beginners  
- Not suitable for CPU-intensive tasks  
- Requires event loop management  

## One-Line Summary
Asyncio coroutines allow multiple tasks to run concurrently without blocking the program.
