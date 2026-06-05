# Process Naming in Multiprocessing

## Description
Shows how to assign and use custom process names.

## What This Code Does
- Defines a function `myFunc()`  
- Retrieves current process name  
- Creates two processes:
  - One with custom name  
  - One with default name  
- Prints start and exit messages for each process  

## Execution Flow
1. Define function `myFunc()`  
2. Create process with custom name  
3. Create process with default name  
4. Start both processes  
5. Each process:
   - Prints its name  
   - Sleeps for 3 seconds  
   - Prints exit message  
6. Main process waits using `join()`  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Identifying processes  
- Debugging multiprocessing programs  
- Managing multiple processes  

## When to Use
Use when:
- You need to track processes  
- Debugging is required  

Avoid when:
- Process naming is not important  

## How to Use
1. Create process using `multiprocessing.Process()`  
2. Assign name using `name` parameter  
3. Access name using `multiprocessing.current_process().name`  

## Advantages
- Easy identification of processes  
- Helpful in debugging  
- Improves code readability  

## Disadvantages
- No performance improvement  
- Adds minor overhead  

## One-Line Summary
Allows assigning and using custom names for processes in multiprocessing.
