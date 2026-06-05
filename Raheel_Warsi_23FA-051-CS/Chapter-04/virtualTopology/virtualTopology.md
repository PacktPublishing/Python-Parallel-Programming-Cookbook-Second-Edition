# MPI Cartesian Topology (mpi4py)

## Description
This code demonstrates the creation of a Cartesian grid topology in MPI, where processes are arranged in a 2D grid and each process identifies its neighboring processes.

## What This Code Does
- Initializes MPI environment  
- Organizes processes into a 2D grid (rows × columns)  
- Creates a Cartesian communicator  
- Finds each process’s position in the grid  
- Identifies neighboring processes (UP, DOWN, LEFT, RIGHT)  
- Prints process location and neighbors  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get total number of processes  
3. Compute grid size (rows and columns)  
4. Create Cartesian topology using `Create_cart()`  
5. Get coordinates of each process in grid  
6. Use `Shift()` to find neighbors:
   - UP / DOWN  
   - LEFT / RIGHT  
7. Print process rank, position, and neighbors  

## How to Execute
1. Install required package:
   ```bash
   pip install mpi4py numpy
