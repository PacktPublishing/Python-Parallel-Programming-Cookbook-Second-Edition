# Process Pool in Multiprocessing

## Description
Shows how to use a process pool to execute tasks in parallel.

## What This Code Does
- Defines a function `function_square()`  
- Creates a list of inputs (0 to 99)  
- Uses a pool of 4 processes  
- Applies the function to all inputs using `map()`  
- Collects and prints results  

## Execution Flow
1. Create input list (0–99)  
2. Create process pool with 4 processes  
3. Apply function using `pool.map()`  
4. Close the pool  
5. Wait for all processes using `join()`  
6. Print output results  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Parallel data processing  
- Batch task execution  
- Large computations  

## When to Use
Use when:
- Same function needs to run on multiple inputs  
- Tasks can be parallelized  

Avoid when:
- Tasks are dependent on each other  
- Small workloads  

## How to Use
1. Create pool using `multiprocessing.Pool()`  
2. Use `map()` to apply function  
3. Close pool using `close()`  
4. Wait using `join()`  

## Advantages
- Easy parallel processing  
- Efficient for large datasets  
- Reduces execution time  

## Disadvantages
- Overhead of process creation  
- Not suitable for small tasks  
- Limited control over individual processes  

## One-Line Summary
Process Pool runs multiple tasks in parallel using a fixed number of processes.
