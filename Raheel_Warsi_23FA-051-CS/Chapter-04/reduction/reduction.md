# MPI Reduce Operation (mpi4py)

## Description
This code demonstrates the use of `Reduce` in MPI, where data from all processes is combined into a single result at the root process.

## What This Code Does
- Initializes MPI environment  
- Each process creates a NumPy array  
- Each process sends its data to root process (0)  
- `Reduce` performs summation of all arrays  
- Result is stored in `recvdata` at root  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank and size  
3. Create send array for each process  
4. Initialize receive array (only used at root)  
5. Each process sends data using `Reduce()`  
6. MPI sums all arrays (`MPI.SUM`)  
7. Root process receives final result  
8. All processes print output  

## How to Execute
1. Install required libraries:
   ```bash
   pip install mpi4py numpy


