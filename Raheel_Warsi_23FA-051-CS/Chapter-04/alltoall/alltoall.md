# MPI Alltoall Communication (mpi4py)

## Description
This code demonstrates parallel communication using `mpi4py`, where each process sends and receives data from all other processes using `Alltoall`.

## What This Code Does
- Initializes MPI environment  
- Gets total number of processes and current process rank  
- Each process creates a data array based on its rank  
- Uses `Alltoall` to exchange data between all processes  
- Prints sent and received data  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get number of processes (`size`)  
3. Get process ID (`rank`)  
4. Each process creates `senddata` array  
5. Create empty `recvdata` array  
6. Perform `Alltoall` communication  
7. Print sent and received values  

## How to Execute
1. Install MPI and mpi4py:
   ```bash
   pip install mpi4py
