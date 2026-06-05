# Daemon vs Non-Daemon Process in Multiprocessing

## Description
Shows the difference between a daemon process and a normal process in Python multiprocessing.

## What This Code Does
- Creates two processes with different names  
- One process is set as daemon (`background_process`)  
- Another process runs normally (`NO_background_process`)  
- Each process prints numbers based on its name  
- Demonstrates background vs foreground execution behavior  

## Execution Flow
1. Define function `foo()`  
2. Create daemon process (`background_process`)  
3. Create normal process (`NO_background_process`)  
4. Start both processes  
5. Each process:
   - Prints start message  
   - Executes loop based on process name  
   - Prints exit message  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Understanding daemon processes  
- Running background tasks  
- Separating critical and non-critical tasks  

## When to Use
Use daemon processes when:
- Task is background/low priority  
- It should stop when main program ends  

Use normal processes when:
- Task must complete fully  
- Data processing is important  

## How to Use
1. Create process using `multiprocessing.Process()`  
2. Set daemon using `daemon=True` or `False`  
3. Start process using `start()`  

## Advantages
- Daemon processes run in background  
- Useful for background services  
- Helps manage process lifecycle  

## Disadvantages
- Daemon processes may stop abruptly  
- Risk of incomplete execution  
- Not suitable for critical tasks  

## One-Line Summary
Daemon processes run in background and stop automatically when the main program ends.
