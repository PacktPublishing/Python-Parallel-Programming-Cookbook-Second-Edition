# MPI Hello World (mpi4py)

## Description
This is a basic MPI program that demonstrates parallel execution by printing a message from each process.

## What This Code Does
- Initializes MPI environment  
- Gets the rank of each process  
- Each process prints "hello world" with its rank  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank using `Get_rank()`  
3. Each process executes independently  
4. Each process prints its rank  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py
