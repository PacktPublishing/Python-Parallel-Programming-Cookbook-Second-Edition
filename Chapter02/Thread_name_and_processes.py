from threading import Thread

# Custom thread class
class MyThreadClass(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("ID of process running {}".format(self.name))


def main():

    # Create thread objects
    thread1 = MyThreadClass("Thread#1")
    thread2 = MyThreadClass("Thread#2")

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for completion
    thread1.join()
    thread2.join()

    print("End")


if __name__ == "__main__":
    main()