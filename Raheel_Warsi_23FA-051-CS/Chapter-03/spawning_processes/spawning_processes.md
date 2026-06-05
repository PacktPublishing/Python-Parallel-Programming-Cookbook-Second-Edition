# Spawn a Process in Multiprocessing

## Description
Shows how to create and run multiple processes using Python multiprocessing by spawning new processes in a loop.

## What This Code Does
- Defines a function `myFunc(i)`  
- Spawns 6 separate processes  
- Each process runs `myFunc` with a different value of `i`  
- Each process prints output based on its input  

## Execution Flow
1. Loop runs from 0 to 5  
2. For each value:
   - A new process is created  
   - Function `myFunc(i)` is assigned as target  
3. Process is started using `start()`  
4. Main program waits using `join()`  
5. Each process:
   - Prints process number  
   - Runs loop from 0 to `i-1`  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Creating multiple independent tasks  
- Parallel execution of functions  
- Process-based task distribution  

## When to Use
Use when:
- Tasks can run independently  
- You want parallel execution  

Avoid when:
- Tasks are very small  
- Overhead of process creation is too high  

## How to Use
1. Define function to run in process  
2. Create process using `multiprocessing.Process()`  
3. Pass arguments using `args=`  
4. Start process using `start()`  
5. Wait using `join()`  

## Advantages
- True parallel execution  
- Useful for CPU-heavy tasks  
- Easy to spawn multiple processes  

## Disadvantages
- High overhead per process  
- Slower for small tasks  
- Memory consumption is higher  

## One-Line Summary
Spawning processes allows running multiple independent tasks in parallel.
