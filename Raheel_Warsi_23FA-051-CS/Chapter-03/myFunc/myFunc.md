# Simple Function in Multiprocessing

## Description
Demonstrates a simple function executed by a process.

## What This Code Does
- Defines a function `myFunc(i)`  
- Prints process number  
- Loops from 0 to `i-1`  
- Prints output values  

## Execution Flow
1. Function is called with argument `i`  
2. Prints process identifier  
3. Runs loop from 0 to `i-1`  
4. Prints each value  

## How to Execute
1. Call this function from a multiprocessing process  
2. Example:
   python main.py  

## End Use
Used for:
- Testing multiprocessing  
- Demonstrating process execution  
- Basic function behavior  

## When to Use
Use when:
- Learning multiprocessing basics  
- Testing process-based functions  

Avoid when:
- Complex logic is required  

## How to Use
1. Define function  
2. Pass it as target in `multiprocessing.Process()`  
3. Provide argument `i`  

## Advantages
- Simple and easy to understand  
- Useful for testing  
- Demonstrates process execution  

## Disadvantages
- Not useful for real applications  
- Only prints output  
- No return value usage  

## One-Line Summary
A simple function used to demonstrate execution inside a process.
