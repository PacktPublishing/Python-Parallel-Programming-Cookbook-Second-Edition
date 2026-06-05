# MPI Send and Receive (Multiple Processes)

## Description
This code demonstrates point-to-point communication in MPI where different processes send and receive data using `send()` and `recv()`.

## What This Code Does
- Initializes MPI environment  
- Multiple processes communicate using ranks  
- Process 0 sends numeric data to process 4  
- Process 1 sends string data to process 8  
- Processes 4 and 8 receive and print data  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank = 0:
   - Send integer data to process 4  
4. If rank = 1:
   - Send string data to process 8  
5. If rank = 4:
   - Receive data from process 0  
6. If rank = 8:
   - Receive data from process 1  
7. Each process prints its rank and received/sent data  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py
