# Pipes in Multiprocessing

## Description
This code demonstrates the use of Pipes in Python multiprocessing.

## What This Code Does
- Creates two processes  
- First process generates numbers from 0 to 9  
- Second process receives numbers and squares them  
- Uses pipes to pass data between processes  
- Main process prints the squared results  

## Execution Flow
1. Create first pipe (`pipe_1`)  
2. Start first process:
   - Sends numbers (0–9) through pipe  
3. Create second pipe (`pipe_2`)  
4. Start second process:
   - Receives numbers from first pipe  
   - Squares each number  
   - Sends result to second pipe  
5. Main process:
   - Receives squared values  
   - Prints output  
6. Ends when all data is processed  

## How to Execute
1. Open terminal in this folder  
2. Run:
   python main.py  

## End Use
Used for:
- Inter-process communication (IPC)  
- Data transfer between processes  
- Building pipelines of processes  

## When to Use
Use when:
- Processes need to communicate  
- Data needs to be passed sequentially between processes  

Avoid when:
- Multiple producers/consumers (use Queue instead)  
- Complex communication is required  

## How to Use
1. Create pipe using `multiprocessing.Pipe()`  
2. Use `send()` to send data  
3. Use `recv()` to receive data  
4. Close unused pipe ends  
5. Handle `EOFError` when data ends  

## Advantages
- Fast communication between processes  
- Simple to implement  
- Suitable for two-way communication  

## Disadvantages
- Limited to two endpoints  
- Not ideal for multiple processes  
- Requires careful closing of pipes  

## One-Line Summary
Pipes allow processes to communicate by sending and receiving data between them.
