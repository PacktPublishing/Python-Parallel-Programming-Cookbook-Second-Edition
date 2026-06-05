# MPI Send and Receive Communication (mpi4py)

## Description
This code demonstrates point-to-point communication in MPI using `send()` and `recv()` between two processes.

## What This Code Does
- Initializes MPI environment  
- Identifies process rank  
- Process 1 and Process 5 exchange messages  
- Uses `send()` and `recv()` for direct communication  
- Each process sends and receives data from the other  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank = 1:
   - Send data `"a"` to process 5  
   - Receive data from process 5  
   - Print sent and received values  
4. If rank = 5:
   - Send data `"b"` to process 1  
   - Receive data from process 1  
   - Print sent and received values  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py
