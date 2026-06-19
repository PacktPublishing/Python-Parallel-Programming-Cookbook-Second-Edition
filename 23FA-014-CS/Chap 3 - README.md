**Chapter 03 — Process-Based Parallelism**

This chapter moves from threads to processes. Each process gets its own memory space, making it ideal for CPU-heavy tasks. We cover creating, naming, killing, and communicating between processes.


**myFunc.py — Helper Function**
Defines myFunc(i) which prints output from a process and loops i times.
Used as the target function by spawning_processes_namespace.py.


**spawning_processes.py — Creating Processes**
Spawns 6 processes, each running myFunc with a different argument.
Each process is started and immediately joined before the next one begins.


**spawning_processes_namespace.py — Importing Function from Another File**
Same as spawning_processes.py but imports myFunc from the separate myFunc.py module.
Shows how to keep code organized by separating the worker function into its own file.


**naming_processes.py — Giving Processes Custom Names**
Creates two processes — one with a custom name, one with the default name.
Each process prints its own name when it starts and exits, so you can tell them apart.


**process_in_subclass.py — Process as a Class**
Defines MyProcess by extending multiprocessing.Process and overriding run().
Spawns 10 instances of it — a cleaner, object-oriented way to create processes.


**run_background_processes.py — Daemon vs Non-Daemon Processes**
Creates one daemon process (daemon=True) and one non-daemon process.
Daemon processes are killed automatically when the main program exits; non-daemons keep running.


**run_background_processes_no_daemons.py — Both Non-Daemon**
Same as above but both processes have daemon=False.
Shows the difference: without a daemon, both processes run to completion regardless of the main program.


**killing_processes.py — Terminating a Process**
Starts a process then immediately calls p.terminate() to stop it.
Prints the process state at each step and checks the exit code (-15 means it was terminated).


**process_pool.py — Process Pool**
Creates a pool of 4 worker processes and uses pool.map() to square numbers 0-99 in parallel.
Much simpler than managing processes manually — the pool distributes the work automatically.


**communicating_with_pipe.py — Talking Between Processes via Pipe**
Uses two Pipe connections to chain processes: one generates numbers 0-9, another squares them.
The main process reads the final squared results from the second pipe.


**communicating_with_queue.py — Sharing Data via Queue**
A producer process puts 10 random numbers into a multiprocessing.Queue.
A consumer process reads and removes items from the queue until it's empty.


**processes_barrier.py — Barrier for Processes**
Two processes use a Barrier to wait for each other before printing their timestamp — they sync up.
Two other processes run without a barrier and print immediately, showing the timing difference.


**Key Concepts**

Process — An independent program with its own memory
daemon=True — Process dies when the main script ends
Pool — A managed group of worker processes
Pipe — A two-way communication channel between 2 processes
Queue — A thread/process-safe data-sharing structure
Barrier — Makes processes wait for each other before continuing
