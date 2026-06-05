# Barrier in Multiprocessing

## Description
Shows how a Barrier synchronizes processes to execute at the same time.

## What This Code Does
- Creates multiple processes  
- Two processes use a Barrier to synchronize  
- Two processes run without synchronization  
- Uses a Lock to control output printing  
- Displays timestamps of process execution  

## Execution Flow
1. Create a Barrier for 2 processes  
2. Create a Lock for synchronized printing  
3. Start two processes with barrier:
   - Wait using `barrier.wait()`  
   - Execute together after synchronization  
4. Start two processes without barrier:
   - Execute immediately  
5. Print process name and timestamp  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Synchronizing multiple processes  
- Coordinating execution timing  
- Parallel task control  

## When to Use
Use when:
- Processes must start together  
- Synchronization point is required  

Avoid when:
- Processes are independent  
- No coordination is needed  

## How to Use
1. Create barrier using `multiprocessing.Barrier()`  
2. Use `wait()` to synchronize processes  
3. Use `Lock` to control shared output  

## Advantages
- Ensures synchronized execution  
- Useful for parallel coordination  
- Improves timing consistency  

## Disadvantages
- Processes may wait longer  
- Depends on slowest process  
- Adds synchronization overhead  

## One-Line Summary
Barrier makes multiple processes wait and execute together at the same point.
