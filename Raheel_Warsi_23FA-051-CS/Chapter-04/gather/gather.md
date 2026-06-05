# MPI Gather Communication (mpi4py)

## Description
This code demonstrates the use of `gather()` in MPI, where all processes send data to a single root process.

## What This Code Does
- Initializes MPI environment  
- Each process generates its own data value  
- All processes send data to process 0 (root)  
- Root process collects and prints all received data  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get total number of processes (`size`)  
3. Get process rank (`rank`)  
4. Each process calculates data: `(rank + 1)^2`  
5. Use `gather()` to send data to root process (0)  
6. Root process:
   - Receives all data  
   - Prints values from all processes  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py
