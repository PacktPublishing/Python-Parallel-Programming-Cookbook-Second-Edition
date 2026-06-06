from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

# Synchronization point for a fixed number of threads
num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    # Simulate runners reaching a checkpoint at different times
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    
    # All threads wait here until the 3rd one calls wait()
    finish_line.wait()

def main():
    threads = []
    print('START RACE!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Race over!')

if __name__ == "__main__":
    main()