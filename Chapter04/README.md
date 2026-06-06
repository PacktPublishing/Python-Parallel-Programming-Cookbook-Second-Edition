**Chapter 04 — Message Passing Interface (MPI)**

This chapter introduces MPI (Message Passing Interface) using the mpi4py library. MPI lets multiple processes running across one or many machines communicate with each other — the foundation of distributed computing.

Note: Run these scripts with "mpiexec -n <num_processes> python <script.py>" instead of python directly.


**helloworld_MPI.py — First MPI Program**
Every process prints "hello world" along with its rank (unique ID number).
The simplest way to confirm MPI is working and see how many processes are running.


**pointToPointCommunication.py — Direct Send and Receive**
Process 0 sends a number to process 4; process 1 sends a string to process 8.
Shows the basic comm.send() / comm.recv() pattern — one process talks directly to another.


**broadcast.py — Send to Everyone at Once**
Process 0 (the root) has a value (100) and broadcasts it to all other processes.
After comm.bcast(), every process holds the same value — no one is left out.


**scatter.py — Split Data Across Processes**
Process 0 has a list of 10 items and scatters one item to each process.
Each process receives its own unique piece — useful for dividing work evenly.


**gather.py — Collect Results from All Processes**
Each process computes (rank+1) squared and sends it back to process 0 via comm.gather().
Process 0 collects all results into one list — the opposite of scatter.


**alltoall.py — Everyone Talks to Everyone**
Each process sends a different chunk of data to every other process simultaneously.
After Alltoall, each process has received one piece from each other process.


**reduction.py — Combine Results with an Operation**
Each process has an array; comm.Reduce() adds them all together and puts the result in process 0.
MPI.SUM is the operation — you can also use MPI.MAX, MPI.MIN, etc.


**deadLockProblems.py — The Deadlock Trap**
Process 1 waits to receive before sending; process 5 sends first then waits to receive.
This mismatch causes a deadlock — both processes end up waiting forever. A classic bug in MPI.


**virtualTopology.py — Grid Layout of Processes**
Arranges all processes into a 2D grid (like a chessboard) using Create_cart().
Each process knows its row/column position and the ranks of its UP, DOWN, LEFT, RIGHT neighbours.


**MPI Communication Patterns**

send / recv — Direct message from one process to another
bcast — One process sends the same data to all
scatter — One process splits data and sends each piece to a different process
gather — All processes send their data back to one process
Alltoall — Every process sends to and receives from every other process
Reduce — Combines data from all processes using an operation (e.g. sum)
