**Chapter 01 — Getting Started with Python**

A warm-up chapter covering Python basics before jumping into parallel programming.


**dir.py — Number Check + List Sum**
Checks if a number is positive, negative, or zero using if/elif/else.
Loops through a list of numbers and prints their total sum.


**flow.py — Control Flow (if, for, while)**
Covers all three main control structures in one file.
if/elif/else for decisions, for to sum a list, while to add 1 to 10.


**lists.py — Python Data Structures**
Shows how to use lists (ordered, changeable), dictionaries (key-value pairs), and tuples (fixed, unchangeable).
Demonstrates updating values and using a function stored in a variable.


**classes.py — Classes and Inheritance**
Defines a class with a shared class variable and a per-object instance variable.
Shows how changing a class variable affects all objects, and how inheritance works.


**file.py — File Read and Write**
Opens test.txt, writes two lines, closes it, then reopens and reads the content back.
A simple demo of Python's built-in file handling.


**do_something.py — Helper Function**
Defines do_something(count, out_list) — generates random numbers and appends them to a list.
Used by serial_test.py, multithreading_test.py, and multiprocessing_test.py as the task to benchmark.


**serial_test.py — Serial Execution (Baseline)**
Runs do_something 10 times one after another.
Measures total time — this is the slowest approach and acts as our benchmark baseline.


**multithreading_test.py — Multithreading**
Creates 10 threads, each running do_something, using Python's threading module.
Due to Python's GIL, threads don't truly run in parallel for CPU tasks, so speedup is limited.


**multiprocessing_test.py — Multiprocessing**
Creates 10 separate processes using Python's multiprocessing module.
Each process runs independently with its own memory — gives true parallelism and is fastest for CPU-heavy work.


**thread_and_processes.py — All-in-One Comparison**
Runs both multithreading and multiprocessing in one script and prints the time for each.
The serial block is commented out. Good for directly comparing all approaches.


**Quick Comparison**

Serial — Not parallel — Best for simple, small tasks
Multithreading — Partially parallel — Best for I/O-bound tasks (network, files)
Multiprocessing — Truly parallel — Best for CPU-heavy tasks (calculations)
