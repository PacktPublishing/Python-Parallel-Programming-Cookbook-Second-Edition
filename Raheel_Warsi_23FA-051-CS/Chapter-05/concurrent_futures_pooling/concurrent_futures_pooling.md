# Concurrent Futures: Sequential, Thread Pool, and Process Pool

## Description
This code demonstrates the difference between sequential execution, thread pool execution, and process pool execution using `concurrent.futures`.

## What This Code Does
- Creates a list of numbers from 1 to 10  
- Defines a heavy counting function  
- Executes tasks in three ways:
  - Sequential execution  
  - ThreadPoolExecutor  
  - ProcessPoolExecutor  
- Measures execution time for each method  

## Execution Flow
1. Create number list  
2. Define `count()` function for heavy computation  
3. Define `evaluate()` function  
4. Run sequential execution:
   - Process items one by one  
5. Run thread pool execution:
   - Execute tasks using threads  
6. Run process pool execution:
   - Execute tasks using processes  
7. Print execution time for each method  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Comparing execution models  
- Parallel and concurrent programming  
- Performance testing  

## When to Use
Use ThreadPoolExecutor when:
- Tasks are I/O-bound  
- Waiting operations are involved  

Use ProcessPoolExecutor when:
- Tasks are CPU-intensive  
- Heavy computation is required  

Avoid when:
- Tasks are very small  
- Parallel overhead is unnecessary  

## How to Use
1. Import `concurrent.futures`  
2. Create executor:
   - `ThreadPoolExecutor()`  
   - `ProcessPoolExecutor()`  
3. Submit tasks using `submit()`  
4. Measure execution time  

## Advantages
- Easy parallel programming  
- Faster execution for suitable tasks  
- Simple API for threads and processes  

## Disadvantages
- Threads affected by GIL for CPU tasks  
- Process creation overhead  
- More memory usage in multiprocessing  

## One-Line Summary
This program compares sequential, thread pool, and process pool execution performance in Python.
