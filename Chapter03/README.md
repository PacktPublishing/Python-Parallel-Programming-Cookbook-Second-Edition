# Chapter 3: Process-Based Parallelism

This chapter focuses on multiprocessing in Python. It demonstrates process creation, process communication, synchronization, process pools, daemon processes, and process management techniques used to achieve parallel execution.

---

## spawning_processes.py

### Concept

Creating and executing processes using the multiprocessing module.

### Execution

Run the script using Python.

### End Use

Performs tasks in separate processes.

### When to Use

When CPU-intensive tasks require parallel execution.

### How to Use

Run the program to create multiple processes and observe their execution.

### Advantages

* True parallelism
* Utilizes multiple CPU cores

### Disadvantages

* Higher memory consumption

---

## spawning_processes_namespace.py

### Concept

Creating processes using functions imported from external modules.

### Execution

Run the script using Python.

### End Use

Improves code modularity and reusability.

### When to Use

When process logic is maintained in separate files.

### How to Use

Run the script to execute imported functions in separate processes.

### Advantages

* Better code organization
* Reusable functionality

### Disadvantages

* Additional file dependencies

---

## process_in_subclass.py

### Concept

Creating custom process classes by inheriting from Process.

### Execution

Run the script using Python.

### End Use

Provides greater control over process behavior.

### When to Use

When custom process implementations are required.

### How to Use

Run the script to create and execute process objects.

### Advantages

* Object-oriented design
* Reusable process classes

### Disadvantages

* More complex than basic process creation

---

## naming_processes.py

### Concept

Assigning and managing process names.

### Execution

Run the script using Python.

### End Use

Helps identify running processes.

### When to Use

When multiple processes are executing simultaneously.

### How to Use

Run the script and observe process names during execution.

### Advantages

* Easier debugging
* Better monitoring

### Disadvantages

* Minor management overhead

---

## run_background_processes.py

### Concept

Using daemon processes that execute in the background.

### Execution

Run the script using Python.

### End Use

Supports background services and helper tasks.

### When to Use

When processes should terminate automatically with the main program.

### How to Use

Run the script and observe daemon process behavior.

### Advantages

* Automatic cleanup
* Suitable for background tasks

### Disadvantages

* Cannot outlive the parent process

---

## run_background_processes_no_daemons.py

### Concept

Executing processes as normal non-daemon processes.

### Execution

Run the script using Python.

### End Use

Allows processes to complete independently.

### When to Use

When tasks must finish even if the parent exits.

### How to Use

Run the script and compare behavior with daemon processes.

### Advantages

* Independent execution
* Complete task processing

### Disadvantages

* Requires explicit management

---

## killing_processes.py

### Concept

Terminating running processes programmatically.

### Execution

Run the script using Python.

### End Use

Stops processes before normal completion.

### When to Use

When a process becomes unresponsive or unnecessary.

### How to Use

Run the script and observe process termination.

### Advantages

* Resource control
* Process management

### Disadvantages

* Risk of incomplete execution

---

## process_pool.py

### Concept

Using a process pool to manage multiple worker processes.

### Execution

Run the script using Python.

### End Use

Efficient execution of repetitive tasks.

### When to Use

When the same operation must be applied to many inputs.

### How to Use

Run the script to process data using worker processes.

### Advantages

* Better resource utilization
* Simplified multiprocessing

### Disadvantages

* Pool management overhead

---

## communicating_with_pipe.py

### Concept

Inter-process communication using Pipes.

### Execution

Run the script using Python.

### End Use

Transfers data between processes.

### When to Use

When processes need direct communication.

### How to Use

Run the script and observe data transmission through pipes.

### Advantages

* Fast communication
* Simple implementation

### Disadvantages

* Limited scalability

---

## communicating_with_queue.py

### Concept

Inter-process communication using Queues.

### Execution

Run the script using Python.

### End Use

Supports safe data sharing between processes.

### When to Use

When multiple processes exchange data.

### How to Use

Run the script and observe producer-consumer communication.

### Advantages

* Process-safe communication
* Easy implementation

### Disadvantages

* Queue management overhead

---

## processes_barrier.py

### Concept

Synchronizing processes using Barrier objects.

### Execution

Run the script using Python.

### End Use

Ensures processes reach a synchronization point before continuing.

### When to Use

When parallel tasks must proceed in phases.

### How to Use

Run the script and compare synchronized and unsynchronized execution.

### Advantages

* Coordinated execution
* Easy synchronization

### Disadvantages

* All processes must reach the barrier
