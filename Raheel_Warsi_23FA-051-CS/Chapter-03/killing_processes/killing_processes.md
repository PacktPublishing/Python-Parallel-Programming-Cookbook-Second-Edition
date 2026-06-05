# Process Lifecycle in Multiprocessing

## Description
Shows how a process is started, terminated, and monitored.

## What This Code Does
- Creates a process to run function `foo`  
- Starts the process  
- Terminates the process before completion  
- Checks process status using `is_alive()`  
- Displays exit code after process ends  

## Execution Flow
1. Create process using `multiprocessing.Process`  
2. Check initial status using `is_alive()`  
3. Start process using `start()`  
4. Terminate process using `terminate()`  
5. Wait using `join()`  
6. Print exit code  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Managing process execution  
- Controlling long-running tasks  
- Monitoring process state  

## When to Use
Use when:
- You need to control process lifecycle  
- You want to stop a process early  

Avoid when:
- Task must complete fully without interruption  

## How to Use
1. Create process using `multiprocessing.Process()`  
2. Start using `start()`  
3. Stop using `terminate()`  
4. Wait using `join()`  
5. Check status using `is_alive()` and `exitcode`  

## Advantages
- Full control over process execution  
- Can terminate unwanted tasks  
- Easy monitoring of process state  

## Disadvantages
- Forced termination may lose data  
- Not safe for critical tasks  
- Can leave resources uncleaned  

## One-Line Summary
Controls how a process starts, runs, and terminates in multiprocessing.
