# Multiprocessing with External Function Import

## Description
This code demonstrates how to use multiprocessing by importing a function from another file and running it in separate processes.

## What This Code Does
- Imports `myFunc` from an external file  
- Creates multiple processes in a loop  
- Runs `myFunc(i)` in each process  
- Executes processes one by one  

## Execution Flow
1. Import function `myFunc` from `myFunc.py`  
2. Loop runs from 0 to 5  
3. For each iteration:
   - Create a new process  
   - Assign `myFunc(i)` as target  
   - Start process using `start()`  
   - Wait for completion using `join()`  

## How to Execute
1. Make sure `myFunc.py` exists in the same folder  
2. Open terminal in this folder  
3. Run:
   python main.py  

## End Use
Used for:
- Modular multiprocessing programs  
- Separating logic into different files  
- Reusable process functions  

## When to Use
Use when:
- Code is split into multiple modules  
- Function reuse is required  
- Cleaner project structure is needed  

Avoid when:
- Single small script is enough  
- Overhead of file separation is unnecessary  

## How to Use
1. Define function in separate file (`myFunc.py`)  
2. Import function into main file  
3. Create process using `multiprocessing.Process()`  
4. Pass function as `target`  
5. Start and join process  

## Advantages
- Better code organization  
- Reusable functions  
- Cleaner project structure  

## Disadvantages
- Requires proper file management  
- Slight overhead of imports  
- Debugging across files can be harder  

## One-Line Summary
This code runs an imported function in separate processes using multiprocessing.
