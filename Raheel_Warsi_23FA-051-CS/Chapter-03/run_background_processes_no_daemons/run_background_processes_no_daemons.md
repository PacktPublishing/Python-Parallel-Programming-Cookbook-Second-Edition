# Multiprocessing: Normal Processes (Daemon = False)

## Description
Shows how normal (non-daemon) processes run in Python multiprocessing.

## What This Code Does
- Creates two processes with different names  
- Both processes are set as non-daemon (`daemon = False`)  
- Each process executes the same function `foo()`  
- Prints output based on process name  
- Demonstrates independent process execution  

## Execution Flow
1. Define function `foo()`  
2. Create `background_process` (daemon = False)  
3. Create `NO_background_process` (daemon = False)  
4. Start both processes  
5. Each process:
   - Prints start message  
   - Runs a loop (different ranges based on name)  
   - Prints exit message  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Running independent processes  
- Ensuring tasks complete fully  
- Parallel execution of workloads  

## When to Use
Use when:
- Tasks must complete completely  
- No background termination is desired  
- Work is important or critical  

Avoid when:
- You need background processes  
- Task should stop with main program  

## How to Use
1. Create processes using `multiprocessing.Process()`  
2. Set `daemon = False`  
3. Start processes using `start()`  

## Advantages
- Processes run fully until completion  
- Reliable execution  
- Suitable for important tasks  

## Disadvantages
- Processes may run longer and consume resources  
- No automatic cleanup like daemon processes  
- Less control over background behavior  

## One-Line Summary
Non-daemon processes run independently and complete their full execution.
