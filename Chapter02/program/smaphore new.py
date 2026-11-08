
import threading
import time

# Only 2 computers are available
computer = threading.Semaphore(2)

def student(name):
    print(name, "is waiting for a computer")

    computer.acquire()

    print(name, "is using a computer")
    time.sleep(2)

    print(name, "has finished using the computer")

    computer.release()


# Main program
students = ["Ali", "Ahmed", "Sara", "Usman", "Zara"]

threads = []

for name in students:
    t = threading.Thread(target=student, args=(name,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All students have finished.")
