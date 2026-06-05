# Barrier in Multithreading

## Description
This code demonstrates the use of a Barrier in Python threading.

## What This Code Does
- Creates 3 threads (runners)
- Each thread waits for a random time (2–5 seconds)
- Each thread prints when it reaches the barrier
- All threads wait at the barrier
- When all threads arrive, they continue together

## Execution Flow
1. Set number of threads (`num_runners = 3`)
2. Create a barrier using `Barrier(num_runners)`
3. Start all threads
4. Each thread:
   - Sleeps for random time
   - Prints arrival time
   - Calls `wait()` on barrier
5. All threads proceed after barrier condition is met
6. Main thread waits using `join()`
7. Print "Race over!"

## How to Execute
1. Open terminal in this folder
2. Run:
   python main.py

## End Use
Used for:
- Thread synchronization
- Coordinating parallel tasks
- Situations where all threads must reach a checkpoint

## When to Use
Use when:
- All threads must wait for each other
- Tasks need synchronization at a common point

Avoid when:
- Threads are independent
- No coordination is required

## How to Use
1. Import `Barrier` from threading
2. Create barrier with number of threads
3. Use `barrier.wait()` inside thread function
4. Start and join threads

## Advantages
- Easy synchronization of threads
- Ensures all threads reach same stage
- Useful for parallel coordination

## Disadvantages
- Threads may wait longer
- Performance depends on slowest thread
- Not useful for independent execution

## One-Line Summary
Barrier blocks threads until all reach a common point, then releases them together.
