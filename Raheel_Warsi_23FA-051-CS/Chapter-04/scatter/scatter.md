# MPI Scatter Communication (mpi4py)

## Description
This code demonstrates the use of `scatter()` in MPI, where data is distributed from one root process to all other processes.

## What This Code Does
- Initializes MPI environment  
- Process 0 creates a list of data  
- Data is split and distributed among all processes  
- Each process receives one element  
- Each process prints its received value  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank = 0:
   - Create list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
4. Other processes set data to `None`  
5. Use `scatter()` to distribute data  
6. Each process receives one value  
7. Print process rank and received value  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py
