# Demonstrates creating a custom Process class

import multiprocessing


class MyProcess(multiprocessing.Process):

    # Code executed when process starts
    def run(self):

        print('called run method in %s' % self.name)

        return


if __name__ == '__main__':

    # Create and execute custom process objects
    for i in range(10):

        process = MyProcess()

        process.start()

        process.join()