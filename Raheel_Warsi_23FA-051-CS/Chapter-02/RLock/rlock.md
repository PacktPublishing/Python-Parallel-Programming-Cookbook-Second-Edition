# RLock (Reentrant Lock) in Multithreading

## Description
This code demonstrates the use of a Reentrant Lock (RLock) in Python threading. 

## What This Code Does
- Creates a shared object `Box` with a counter (`total_items`)  
- Uses `RLock` to safely modify shared data  
- One thread adds items  
- Another thread removes items  
- Both threads update the same resource safely  

## Execution Flow
1. Create a `Box` object with `RLock`  
2. Start two threads:
   - Adder thread → adds items  
   - Remover thread → removes items  
3. Each operation:
   - Acquires lock using `with self.lock`  
   - Updates shared variable (`total_items`)  
4. Threads run concurrently but safely  
5. Main thread waits using `join()`  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Safe access to shared resources  
- Nested locking situations  
- Avoiding deadlocks in recursive calls  

## When to Use
Use when:
- Same thread needs to acquire lock multiple times  
- Nested function calls use the same lock  

Avoid when:
- Simple locking is enough (use `Lock`)  
- No shared data is involved  

## How to Use
1. Create lock using `threading.RLock()`  
2. Use `with lock:` to acquire and release safely  
3. Call locked functions inside other locked functions  

## Advantages
- Prevents deadlock in nested locking  
- Allows same thread to re-acquire lock  
- Safe for complex operations  

## Disadvantages
- Slightly slower than normal Lock  
- More complex to understand  
- Overhead if not needed  

## One-Line Summary
RLock allows a thread to acquire the same lock multiple times safely without deadlock.
