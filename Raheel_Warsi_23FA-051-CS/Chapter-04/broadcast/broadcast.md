# MPI Broadcast (mpi4py)

## Description
This code demonstrates broadcasting using `mpi4py`, where one process shares data with all other processes.

## What This Code Does
- Initializes MPI environment  
- Process 0 creates a variable  
- All other processes start with `None`  
- Uses `bcast()` to broadcast value from root process  
- All processes receive the same value  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank is 0:
   - Set variable value (100)  
4. Other processes set variable to `None`  
5. Use `comm.bcast()` to broadcast value  
6. All processes receive same value  
7. Print process rank and received value  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py
