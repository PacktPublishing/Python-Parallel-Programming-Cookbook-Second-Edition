# Multiprocessing Example

## Description
This code demonstrates how to use multiprocessing in Python to run tasks in parallel. 

## What This Code Does
- Runs a function `do_something` in parallel using 10 processes  
- Each process handles a large task (`size = 10,000,000`)  
- Measures total execution time  

## Execution Flow
1. Create 10 processes  
2. `start()` → runs all processes  
3. `join()` → waits until all processes finish  
4. Prints total execution time  

## End Use
Used for heavy CPU tasks such as:
- Data processing  
- Simulations  
- Large calculations  

## When to Use
Use when:
- Task is CPU-intensive  
- Work can run in parallel  

Avoid when:
- Task is small or simple  
- Frequent shared data is required  

## How to Use
1. Define the function (`do_something`)  
2. Create processes using `multiprocessing.Process`  
3. Start processes using `start()`  
4. Wait for completion using `join()`  

## Advantages
- Faster execution  
- Utilizes multiple CPU cores  
- Efficient for heavy tasks  

## Disadvantages
- High memory usage  
- Difficult to debug  
- Data sharing is complex  
- Not efficient for small tasks  

## One-Line Summary
Multiprocessing runs tasks in parallel to reduce execution time.
