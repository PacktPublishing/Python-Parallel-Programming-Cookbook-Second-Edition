# Asyncio Tasks for Parallel Math Functions

## Description
This code demonstrates parallel execution of multiple mathematical functions using `asyncio.Task`.

## What This Code Does
- Defines three asynchronous coroutines:
  - Factorial calculation  
  - Fibonacci calculation  
  - Binomial coefficient calculation  
- Executes all tasks concurrently using `asyncio.Task`  
- Uses asynchronous delays with `asyncio.sleep()`  
- Prints results after computation  

## Execution Flow
1. Define asynchronous math functions  
2. Create tasks using `asyncio.Task()`:
   - `factorial(10)`  
   - `fibonacci(10)`  
   - `binomial_coefficient(20,10)`  
3. Create asyncio event loop  
4. Run all tasks concurrently using `asyncio.wait()`  
5. Print outputs of each function  
6. Close event loop  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Concurrent task execution  
- Mathematical simulations  
- Non-blocking asynchronous programming  

## When to Use
Use when:
- Multiple independent tasks can run together  
- Non-blocking execution is needed  
- Concurrent workflows are required  

Avoid when:
- Tasks are CPU-intensive  
- Sequential execution is preferred  

## How to Use
1. Import `asyncio`  
2. Define coroutines using `@asyncio.coroutine`  
3. Create tasks using `asyncio.Task()`  
4. Run tasks with `asyncio.wait()`  
5. Use event loop to execute tasks  

## Advantages
- Concurrent task execution  
- Lightweight compared to threads  
- Efficient asynchronous programming  

## Disadvantages
- Not suitable for heavy CPU tasks  
- More difficult to understand for beginners  
- Uses older coroutine syntax  

## One-Line Summary
This program runs multiple mathematical computations concurrently using asyncio tasks.
