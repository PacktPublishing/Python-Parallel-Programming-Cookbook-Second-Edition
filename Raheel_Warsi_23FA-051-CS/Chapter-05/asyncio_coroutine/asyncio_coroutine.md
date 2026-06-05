# Finite State Machine using Asyncio Coroutines

## Description
This code demonstrates a Finite State Machine (FSM) simulation using `asyncio` coroutines in Python.

## What This Code Does
- Simulates multiple states using coroutines  
- Randomly transitions between states  
- Uses asynchronous execution with `yield from`  
- Ends when the program reaches `end_state()`  

## Execution Flow
1. Start from `start_state()`  
2. Random value decides next state  
3. Program transitions between:
   - `state1()`  
   - `state2()`  
   - `state3()`  
4. Each state:
   - Prints transition information  
   - Waits for 1 second  
   - Chooses next state randomly  
5. Execution stops at `end_state()`  
6. Event loop runs all coroutine transitions  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- State machine simulation  
- Workflow management  
- Asynchronous state transitions  
- AI/game logic systems  

## When to Use
Use when:
- System behavior depends on states  
- Asynchronous transitions are needed  
- Event-driven workflows are required  

Avoid when:
- Simple linear execution is enough  
- No state transitions are required  

## How to Use
1. Import `asyncio`  
2. Define states as coroutines  
3. Use `yield from` for transitions  
4. Create event loop  
5. Start execution using `run_until_complete()`  

## Advantages
- Clear state-based design  
- Asynchronous execution  
- Flexible workflow transitions  

## Disadvantages
- Complex for large state systems  
- Harder to debug recursive transitions  
- Uses old coroutine syntax (`@asyncio.coroutine`)  

## One-Line Summary
This program simulates a finite state machine using asynchronous coroutines and random state transitions.
