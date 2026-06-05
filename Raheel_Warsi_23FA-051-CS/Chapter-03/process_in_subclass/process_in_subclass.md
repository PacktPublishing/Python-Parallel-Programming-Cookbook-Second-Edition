# Custom Process Class in Multiprocessing

## Description
Shows how to create a custom process by extending the Process class.

## What This Code Does
- Defines a class `MyProcess` that inherits from `multiprocessing.Process`  
- Overrides the `run()` method  
- Creates 10 process instances  
- Each process prints its name when executed  

## Execution Flow
1. Create custom class extending `Process`  
2. Override `run()` method  
3. Loop 10 times:
   - Create process object  
   - Start process using `start()`  
   - Wait using `join()`  
4. Each process executes `run()` method  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Customizing process behavior  
- Object-oriented multiprocessing  
- Managing complex tasks  

## When to Use
Use when:
- You need custom logic inside processes  
- Object-oriented structure is required  

Avoid when:
- Simple function-based process is enough  

## How to Use
1. Create class inheriting from `multiprocessing.Process`  
2. Override `run()` method  
3. Create object and call `start()`  

## Advantages
- Clean and organized code  
- Easy to extend functionality  
- Reusable process logic  

## Disadvantages
- Slightly more complex than simple functions  
- Overhead of class structure  

## One-Line Summary
Custom process class allows defining process behavior using object-oriented programming.
