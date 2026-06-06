import threading

# Function executed by each thread
def my_func(thread_number):
    print('my_func called by thread N°{}'.format(thread_number))


def main():
    threads = []

    # Create and execute 10 threads
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)

        t.start()
        t.join()


if __name__ == "__main__":
    main()