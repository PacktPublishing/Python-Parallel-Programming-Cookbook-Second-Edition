# Semaphore Synchronization

This Python program demonstrates **thread synchronization using semaphores**.

It simulates 5 students sharing 2 available computers. The semaphore allows only 2 students to use computers at the same time, while the remaining students wait until a computer becomes available.

- `acquire()` reserves a computer.
- `release()` frees a computer.
- `threading.Thread()` creates a separate thread for each student.
- `join()` waits for all threads to finish.

**Purpose:** To demonstrate how semaphores control access to limited shared resources in multithreading.